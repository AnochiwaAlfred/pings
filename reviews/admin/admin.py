from django.contrib import admin
from reviews.models import *

# Register your models here.


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = REPORT_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'Reports'
        
@admin.register(UserBlock)
class UserBlockAdmin(admin.ModelAdmin):
    list_display = USER_BLOCK_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'User Blocks'
        