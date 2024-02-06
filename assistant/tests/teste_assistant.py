from channels.testing import WebsocketCommunicator
from core.asgi import application  
import json
import pytest


@pytest.mark.asyncio
async def test_assistant_consumer_connection_and_message():
    communicator = WebsocketCommunicator(application, "ws://localhost:8001/ws/assistant/?api_key=chave_teste")
    connected, _ = await communicator.connect()
    assert connected

    # Envia uma mensagem e verifica a resposta
    test_message = {"message": "Teste"}
    await communicator.send_to(json.dumps(test_message))
    response = await communicator.receive_from(timeout=5)
    assert json.loads(response) == test_message

    # Fecha a conexão
    await communicator.disconnect()
