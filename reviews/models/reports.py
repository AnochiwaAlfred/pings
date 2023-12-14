from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.

REPORT_LIST_DISPLAY = ["id", "user"]


class Report(CoreBaseModel):
    user = models.OneToOneField('users.CustomUser', related_name='reports', on_delete=models.CASCADE, null=True, blank=True)
    message = models.ForeignKey('messaging.Message', on_delete=models.CASCADE, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"Report - {self.id}"
    
    def custom_list_display():
        return REPORT_LIST_DISPLAY
