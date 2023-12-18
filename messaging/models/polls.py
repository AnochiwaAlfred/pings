from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.

POLL_LIST_DISPLAY = ["id", "question", "creator"]


class Poll(CoreBaseModel):
    question = models.CharField(max_length=255, null=True, blank=True)
    options = models.ManyToManyField('messaging.PollOption', related_name='options', blank=True)
    creator = models.ForeignKey('users.CustomUser', related_name='created_polls', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"Poll - {self.id}"
    
    def custom_list_display():
        return POLL_LIST_DISPLAY
