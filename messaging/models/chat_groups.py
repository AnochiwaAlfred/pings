from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.

CHAT_GROUP_LIST_DISPLAY = ["id", "name"]

class ChatGroup(CoreBaseModel):
    name = models.CharField(max_length=255, unique=True)
    members = models.ManyToManyField('users.CustomUser', related_name='chat_groups')
    group_picture = models.ImageField(null=True, blank=True, upload_to='chat_group_pictures/')

    def __str__(self):
        return self.name
    
    def custom_list_display():
        return CHAT_GROUP_LIST_DISPLAY
