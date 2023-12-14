from django.contrib import admin
from notifications.models import *

# Register your models here.


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = DEVICE_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'Devices'


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = NOTIFICATION_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'Notifications'