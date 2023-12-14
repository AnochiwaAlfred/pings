from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.


MESSAGE_LIST_DISPLAY = ["id", "sender", "receiver", "is_read"]


class Message(CoreBaseModel):
    sender = models.ForeignKey('users.CustomUser', related_name='sent_messages', on_delete=models.CASCADE, null=True, blank=True)
    receiver = models.ForeignKey('users.CustomUser', related_name='received_messages', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    # Additional fields for multimedia messages if needed
    image = models.ImageField(upload_to='message_images/', null=True, blank=True)
    video = models.FileField(upload_to='message_videos/', null=True, blank=True)
    file = models.FileField(upload_to='message_files/', null=True, blank=True)

    def __str__(self):
        return f"Message - {self.id}"
    
    def custom_list_display():
        return MESSAGE_LIST_DISPLAY