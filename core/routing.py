# meuprojeto/routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from assistant import consumers

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/somepath/', consumers.MyConsumer.as_asgi()),
    ]),
})
