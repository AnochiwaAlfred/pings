from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.

USER_BLOCK_LIST_DISPLAY = ["id", "user"]


class UserBlock(CoreBaseModel):
    user = models.ForeignKey('users.CustomUser', related_name='blocked_users', on_delete=models.CASCADE)
    blocked_user = models.ForeignKey('users.CustomUser', related_name='blocked_by_users', on_delete=models.CASCADE)
    def __str__(self):
        return f"UserBlock - {self.id}"
    
    def custom_list_display():
        return USER_BLOCK_LIST_DISPLAY