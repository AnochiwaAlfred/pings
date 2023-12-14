from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.

USER_PROFILE_LIST_DISPLAY = ["id", "user"]


class UserProfile(CoreBaseModel):
    user = models.OneToOneField('users.CustomUser', related_name='profile', on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"UserProfile - {self.id}"
    
    def custom_list_display():
        return USER_PROFILE_LIST_DISPLAY