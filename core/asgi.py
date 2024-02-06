import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Importante: Chame get_asgi_application() antes de importar demais dependências do Channels
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import assistant.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,  # Assegura que o Django é inicializado primeiro para HTTP
    "websocket": AuthMiddlewareStack(
        URLRouter(
            assistant.routing.websocket_urlpatterns
        )
    ),
})
