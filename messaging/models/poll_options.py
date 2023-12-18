from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.


POLL_OPTION_LIST_DISPLAY = ["id", "context"]


class PollOption(CoreBaseModel):
    # poll = models.ForeignKey('messaging.Poll', related_name='options', on_delete=models.CASCADE, null=True, blank=True)
    context = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return f"Poll Option - {self.id}"
    
    def custom_list_display():
        return POLL_OPTION_LIST_DISPLAY
