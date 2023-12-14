from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.

CUSTOM_EMOTICON_LIST_DISPLAY = ["id", "user", "shortcut"]


class CustomEmoticon(CoreBaseModel):
    user = models.ForeignKey('users.CustomUser', related_name='custom_emoticons', on_delete=models.CASCADE)
    shortcut = models.CharField(max_length=50, unique=True, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='custom_emoticons/')

    def __str__(self):
        return f"Emoticon - {self.id}"
    
    def custom_list_display():
        return CUSTOM_EMOTICON_LIST_DISPLAY