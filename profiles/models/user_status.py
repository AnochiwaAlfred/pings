from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.


USER_STATUS_LIST_DISPLAY = ["id", "user"]


class UserStatus(CoreBaseModel):
    user = models.OneToOneField('users.CustomUser', related_name='status', on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    last_online = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"UserStatus - {self.id}"
    
    def custom_list_display():
        return USER_STATUS_LIST_DISPLAY
