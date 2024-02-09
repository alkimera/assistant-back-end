from channels.generic.websocket import AsyncWebsocketConsumer
import json
from urllib.parse import parse_qs
from assistant.tools import OpenAIAssistantClient


class AssistantConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('tentando')
        query_string = parse_qs(self.scope['query_string'].decode())
        api_key = query_string.get('api_key', [None])[0]
        
        if api_key == "chave_teste":
            await self.accept()
        else:
            await self.close(code=403)

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        client = OpenAIAssistantClient()
        text_data_json = json.loads(text_data)
        message = client.create_thread_and_run_assistant(text_data_json['message'])
        
        await self.send(text_data=json.dumps({
            'message': message
        }))