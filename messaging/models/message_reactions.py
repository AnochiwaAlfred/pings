from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.



MESSAGE_REACTION_LIST_DISPLAY = ["id", "message", "user", "emoji"]


class MessageReaction(CoreBaseModel):
    message = models.ForeignKey('messaging.Message', related_name='reactions', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey('users.CustomUser', related_name='message_reactions', on_delete=models.CASCADE, blank=True, null=True)
    emoji = models.CharField(max_length=255)

    def __str__(self):
        return f"Message Reaction - {self.id}"
    
    def custom_list_display():
        return MESSAGE_REACTION_LIST_DISPLAY