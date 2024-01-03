from django.shortcuts import get_object_or_404
from ninja import File, Router, FormEx
from ninja.files import UploadedFile
from typing import List, Union
from plugins.hasher import hasherGenerator
from users.models import *
from notifications.models import *
from schemas.notifications import *
from django.db.models import Q

router = Router(tags=["Notifications & Devices Endpoints"])


@router.get('list_all_devices/', response=List[DeviceRetrievalSchema])
def list_devices(request):
    """Get a list of all registered devices"""
    return Device.objects.all()


@router.get('{user_id}/list_all_devices/', response=List[DeviceRetrievalSchema])
def list_user_devices(request, user_id):
    """Get a list of a user's registered devices"""
    return Device.objects.filter(user_id=user_id)


@router.get('device/{device_id}/get/', response=Union[DeviceRetrievalSchema, str])
def get_device(request, device_id):
    """Get a specific device details"""
    device = get_object_or_404(Device, id=device_id)
    return device


@router.post('device/create', response=DeviceRetrievalSchema)
def add_device(request, user_id):
    hh = hasherGenerator()
    device_token = hh.get("token").decode("utf-8")
    device = Device.objects.create(user_id=user_id, device_token=device_token)
    return device
    

@router.get('device/{device_id}/delete/')
def delete_device(request, device_id):
    """Delete a specific device """
    device = get_object_or_404(Device, id=device_id)
    if device:
        device.delete()
        return f"Device {device.id} deleted successfully"
    return device

    



@router.get('list_all_notifications/', response=List[NotificationRetrievalSchema])
def list_notifications(request):
    """Get a list of all registered notifications"""
    return Notification.objects.all()


@router.get('{user_id}/list_all_notifications/', response=List[NotificationRetrievalSchema])
def list_user_notifications(request, user_id):
    """Get a list of a user's registered notifications"""
    notifications = Notification.objects.filter(user_id=user_id).order_by('-timestamp')
    notifications2 = []
    for item in notifications:
        notification = NotificationRetrievalSchema(
            id=item.id,
            # sender=item.sender,
            content=item.content,
            timestamp=item.timestamp,
            is_read=item.is_read,
            sender = NotificationAuthRetrievalSchema(
                id=item.sender.id,
                display_name=item.sender.display_name,
                image=request.build_absolute_uri(item.sender.image.url) if item.sender.image else "",
                is_online=item.sender.is_online
            )
        )
        notifications2.append(notification)
    return notifications2


@router.get('{user_id}/list_all_unread_notifications/', response=List[NotificationRetrievalSchema])
def list_user_unread_notifications(request, user_id):
    """Get a list of a user's unread notifications"""
    return Notification.objects.filter(user_id=user_id, is_read=False)


@router.get('notification/{notification_id}/get/', response=Union[NotificationRetrievalSchema, str])
def get_notification(request, notification_id):
    """Get a specific notification details"""
    notification = get_object_or_404(Notification, id=notification_id)
    return notification


@router.post('notification/create', response=NotificationRetrievalSchema)
def add_notification(request, notificationData:NotificationRegistrationSchema=FormEx(None)):
    notification = Notification.objects.create(**notificationData)
    return notification


@router.patch('notification/{notification_id}/mark_as_read', response=NotificationRetrievalSchema)
def mark_notification_as_read(request, notification_id):
    """Mark a notification as read"""
    notification = get_object_or_404(Notification, id=notification_id)
    if notification:
        notification.is_read=True
        notification.save()
    return notification
    

@router.get('notification/{notification_id}/delete/')
def delete_notification(request, notification_id):
    """Delete a specific notification """
    notification = get_object_or_404(Notification, id=notification_id)
    if notification:
        notification.delete()
        return f"Notification {notification.id} deleted successfully"
    return notification

    