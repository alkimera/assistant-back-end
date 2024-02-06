from channels.generic.websocket import AsyncWebsocketConsumer
import json
from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from assistant.models import Carrinho, Comida


class CartConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        query_string = parse_qs(self.scope['query_string'].decode())
        self.token = query_string.get('token', [None])[0]
        if self.token:
            await self.accept()
        else:
            await self.close(code=403)

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        action = text_data_json['action']
        
        if action == 'add':
            await self.add_to_cart(text_data_json['comida_id'], text_data_json.get('quantidade', 1))
            await self.send(text_data=json.dumps({'status': 'item adicionado'}))
            
        elif action == 'remove':
            await self.remove_from_cart(text_data_json['comida_id'])
            await self.send(text_data=json.dumps({'status': 'item removido'}))
            
        elif action == 'view':
            cart_items = await self.get_cart_items()
            await self.send(text_data=json.dumps({'cart': cart_items}))
            

    @database_sync_to_async
    def add_to_cart(self, comida_id, quantidade):
        comida, _ = Comida.objects.get_or_create(id=comida_id)
        carrinho, created = Carrinho.objects.get_or_create(token=self.token, comida=comida)
        if not created:
            carrinho.quantidade += quantidade
            carrinho.save()
        return carrinho

    @database_sync_to_async
    def remove_from_cart(self, comida_id):
        Carrinho.objects.filter(token=self.token, comida_id=comida_id).delete()
        return None

    @database_sync_to_async
    def get_cart_items(self):
        items = Carrinho.objects.filter(token=self.token).values('comida__comida', 'quantidade')
        return list(items)