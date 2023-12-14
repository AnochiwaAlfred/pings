from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.


FRIENDSHIP_LIST_DISPLAY = ["id", "user", "friend"]


class Friendship(CoreBaseModel):
    user = models.ForeignKey('users.CustomUser', related_name='friendships', on_delete=models.CASCADE, null=True, blank=True)
    friend = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"Friendship - {self.id}"
    
    def custom_list_display():
        return FRIENDSHIP_LIST_DISPLAY