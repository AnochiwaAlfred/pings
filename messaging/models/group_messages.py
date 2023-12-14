from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.


GROUP_MESSAGE_LIST_DISPLAY = ["id", "group", "sender", "timestamp"]


class GroupMessage(CoreBaseModel):
    group = models.ForeignKey('messaging.ChatGroup', related_name='group_messages', on_delete=models.CASCADE, blank=True, null=True)
    sender = models.ForeignKey('users.CustomUser', related_name='sent_group_messages', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Group Message - {self.id}"
    
    def custom_list_display():
        return GROUP_MESSAGE_LIST_DISPLAY