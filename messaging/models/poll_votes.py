from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.


POLL_VOTE_LIST_DISPLAY = ["id", "user", "poll", "selected_option"]


class PollVote(CoreBaseModel):
    user = models.ForeignKey('users.CustomUser', related_name='poll_votes', on_delete=models.CASCADE, null=True, blank=True)
    poll = models.ForeignKey('messaging.Poll', related_name='votes', on_delete=models.CASCADE, null=True, blank=True)
    selected_option = models.ForeignKey('messaging.PollOption', related_name='poll_options', on_delete=models.CASCADE, null=True, blank=True)
    # selected_option = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return f"Poll Vote - {self.id}"
    
    def custom_list_display():
        return POLL_VOTE_LIST_DISPLAY
