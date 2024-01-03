"""
For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pings.settings')
from pings.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    # Django (HTTP) requests are handled by the ASGI server internal to Django.
    "http": get_asgi_application(),
    # WebSocket connections are handled by a separate module that runs in its own thread.
    # See http://channels.readthedocs.org/en/latest/topics/channel_layers.html for more details
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
