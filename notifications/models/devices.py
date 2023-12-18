from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.

DEVICE_LIST_DISPLAY = ["id", "user", "device_token"]


class Device(CoreBaseModel):
    user = models.ForeignKey('users.CustomUser', related_name='devices', on_delete=models.CASCADE, null=True, blank=True)
    device_token = models.CharField(max_length=255, null=True, blank=True, unique=True)
    def __str__(self):
        return f"Device - {self.id}"
    
    def custom_list_display():
        return DEVICE_LIST_DISPLAY