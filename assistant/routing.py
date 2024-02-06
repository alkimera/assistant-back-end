from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/assistant/$', consumers.AssistantConsumer.as_asgi()),
    re_path(r'ws/cart/$', consumers.CartConsumer.as_asgi()),
]
