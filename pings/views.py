from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_message_to_websocket(message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("chat_group_1", {"type": "chat.message", "message": message})
    