from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.


USER_SETTING_LIST_DISPLAY = ["id", "user"]


class UserSetting(CoreBaseModel):
    user = models.OneToOneField('users.CustomUser', related_name='settings', on_delete=models.CASCADE)
    theme = models.CharField(max_length=255, choices=[('light', 'Light'), ('dark', 'Dark')], default='light')
    notification_preferences = models.JSONField(default=dict)
    def __str__(self):
        return f"UserSetting - {self.id}"
    
    def custom_list_display():
        return USER_SETTING_LIST_DISPLAY