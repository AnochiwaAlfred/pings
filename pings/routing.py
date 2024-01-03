from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/room_name/$', consumers.ChatConsumer.as_asgi())
]