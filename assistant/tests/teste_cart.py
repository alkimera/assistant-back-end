import pytest
from channels.testing import WebsocketCommunicator
import json
from django.conf import settings
from core.asgi import application  
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async
from assistant.models import Comida

@pytest.mark.django_db(transaction=True)
@pytest.mark.asyncio
async def test_cart_consumer_add_view_remove():
    comida_teste = await database_sync_to_async(Comida.objects.create)(comida="Pizza")

    communicator = WebsocketCommunicator(application, f"ws://localhost:8001/ws/cart/?token=token_teste")
    connected, _ = await communicator.connect()
    assert connected

    await communicator.send_to(json.dumps({
        "action": "add",
        "comida_id": comida_teste.id,
        "quantidade": 1
    }))
    response = await communicator.receive_from(timeout=5)
    assert json.loads(response) == {"message": f"{comida_teste.comida} adicionado ao carrinho"}

    await communicator.send_to(json.dumps({"action": "view"}))
    response = await communicator.receive_from()
    expected_response = {'cart': [{'comida__comida': comida_teste.comida, 'quantidade': 1}]}
    assert json.loads(response) == expected_response

    await communicator.send_to(json.dumps({
        "action": "remove",
        "comida_id": comida_teste.id
    }))
    response = await communicator.receive_from()
    assert json.loads(response) == {"message": f"{comida_teste.comida} removido do carrinho"}

    await communicator.disconnect()
