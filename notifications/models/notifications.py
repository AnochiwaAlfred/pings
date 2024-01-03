from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.

NOTIFICATION_LIST_DISPLAY = ["id", "user", "sender", "timestamp", 'is_read']


class Notification(CoreBaseModel):
    user = models.ForeignKey('users.CustomUser', related_name='notifications', on_delete=models.CASCADE, null=True, blank=True)
    sender = models.ForeignKey('users.CustomUser', related_name='notifications_sender', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    def __str__(self):
        return f"Notification - {self.id}"
    
    def custom_list_display():
        return NOTIFICATION_LIST_DISPLAY