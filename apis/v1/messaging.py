from django.shortcuts import get_object_or_404
from ninja import File, Router, FormEx
from ninja.files import UploadedFile
from typing import List, Union
from users.models import *
from messaging.models import *
from schemas.messaging import *
from django.db.models import Q

router = Router(tags=["Messaging Endpoints"])


# MESSAGE ENDPOINTS

@router.get('list_all_messages/', response=List[MessageRetrievalSchema])
def list_messages(request):
    """Get a list of all registered messages"""
    return Message.objects.all()


@router.get('{user_id}/sent_messages/', response=List[MessageRetrievalSchema])
def list_all_user_sent_messages(request, user_id):
    """Get a list of all user sent messages"""
    return Message.objects.filter(sender_id=user_id)


@router.get('{user_id}/received_messages/', response=List[MessageRetrievalSchema])
def list_all_user_received_messages(request, user_id):
    """Get a list of all user received messages"""
    return Message.objects.filter(receiver_id=user_id)


@router.get('{user_id}/messages/', response=List[MessageRetrievalSchema])
def list_all_user_messages(request, user_id):
    """Get a list of all user messages, sent or received"""
    return Message.objects.filter(Q(sender_id=user_id) | Q(receiver_id=user_id))


@router.get('{user1_id}/{user2_id}/messages/', response=List[MessageRetrievalSchema])
def list_all_messages_between_two_users(request, user1_id, user2_id):
    """Get a list of all messages between two users"""
    return Message.objects.filter(Q(sender_id=user1_id) | Q(receiver_id=user1_id) | Q(sender_id=user2_id) | Q(receiver_id=user2_id))


@router.get('{sender_id}/{receiver_id}/messages_sender_receiver/', response=List[MessageRetrievalSchema])
def list_all_messages_from_sender_to_receiver(request, sender_id, receiver_id):
    """Get a list of all messages from a sender (defined by the first parameter) to a receiver (defined by the second parameter)"""
    return Message.objects.filter(sender_id=sender_id, receiver_id=receiver_id)

@router.get('{message_id}/get/', response=MessageRetrievalSchema)
def get_message(request, message_id):
    """Get a specific message details"""
    message = get_object_or_404(Message, id=message_id)
    return message

@router.post('send_message/', response=MessageRetrievalSchema)
def send_message(request, messageData:MessageRegistrationSchema):
    """Send a text message"""
    message = Message.objects.create(**messageData.dict())
    return message

@router.post('send_multimedia_message/', response=Union[MessageRetrievalSchema, str])
def send_multimedia_message(request, image:UploadedFile=FileEx(None), video:UploadedFile=FileEx(None), file:UploadedFile=FileEx(None)):
    """Send a multimedia message"""
    try:
        if image!=None or video!=None or file!=None:
            message = Message.objects.create(image=image, video=video, file=file)
            return message
        raise ValueError("Empty request body")
    except ValueError as e:
        return str(e)
    
@router.delete('{message_id}/delete/')
def delete_message(request, message_id):
    """Delete a specific message"""
    message = get_object_or_404(Message, id=message_id)
    if message:
        message.delete()
        return "Message {message.id} deleted successfully"
    return message



# MESSAGE ENDPOINTS
# GROUP ENDPOINTS
# GROUP_MESSAGE ENDPOINTS
# POLL ENDPOINTS
# POLL_VOTE ENDPOINTS
# CUSTOM_EMOTICON ENDPOINTS
# MESSAGE_REACTION ENDPOINTS
