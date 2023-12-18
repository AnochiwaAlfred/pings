from django.shortcuts import get_object_or_404
from ninja import File, Router, FormEx
from ninja.files import UploadedFile
from typing import List, Union
from users.models import *
from messaging.models import *
from schemas.messaging import *
from django.db.models import Q

router = Router(tags=["Group Messages Endpoints"])


@router.get('list_all_group_messages/', response=List[GroupMessageRetrievalSchema])
def list_group_messages(request):
    """Get a list of all group messages"""
    return GroupMessage.objects.all()

@router.get('group/{group_id}/list_all_group_messages/', response=List[GroupMessageRetrievalSchema])
def list_group_messages_by_group(request, group_id):
    """Get a list of all group messages in a particular group"""
    return GroupMessage.objects.filter(group_id=group_id)

@router.get('group/{group_id}/{sender_id}/list_all_group_messages/', response=List[GroupMessageRetrievalSchema])
def list_group_messages_by_group(request, group_id, sender_id):
    """Get a list of all group messages in a particular group by a particular user"""
    return GroupMessage.objects.filter(group_id=group_id, sender_id=sender_id)


@router.get('group_message/{group_message_id}/get/', response=Union[GroupMessageRetrievalSchema, str])
def get_group_message(request, group_message_id):
    """Get a specific group_message details"""
    group_message = get_object_or_404(GroupMessage, id=group_message_id)
    return group_message

@router.post('send_group_message/', response=GroupMessageRetrievalSchema)
def send_group_message(request, groupMessageData:GroupMessageRegistrationSchema=FormEx(None)):
    """Send a text group_message"""
    group_message = GroupMessage.objects.create(**groupMessageData.dict())
    return group_message

@router.delete('group_message/{group_message_id}/delete/')
def delete_group_message(request, group_message_id):
    """Delete a specific group_message"""
    group_message = get_object_or_404(GroupMessage, id=group_message_id)
    if group_message:
        group_message.delete()
        return "Group Message {group_message.id} deleted successfully"
    return group_message
