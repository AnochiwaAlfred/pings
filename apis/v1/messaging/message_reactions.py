from django.shortcuts import get_object_or_404
from ninja import File, Router, FormEx
from ninja.files import UploadedFile
from typing import List, Union
from users.models import *
from messaging.models import *
from schemas.messaging import *
from django.db.models import Q


router = Router(tags=["Message Reactions Endpoints"])

@router.get('list_all_message_reactions/', response=List[MessageReactionRetrievalSchema])
def list_message_reactions(request):
    """Get a list of all registered message reactions"""
    return MessageReaction.objects.all()


@router.get('message_reaction/{message_reaction_id}/get/', response=Union[MessageReactionRetrievalSchema, str])
def message_reaction(request, message_reaction_id):
    """Get a specific message reaction details"""
    message_reaction = get_object_or_404(MessageReaction, id=message_reaction_id)
    return message_reaction
    

@router.post('message_reaction/add', response=MessageReactionRetrievalSchema)
def create_message_reaction(request, MessageReactionData:MessageReactionRegistrationSchema=FormEx(None)):
    """Create a new message_reaction"""
    message_reaction = MessageReaction.objects.create(**MessageReactionData.dict())
    return message_reaction



@router.delete('message_reaction/{message_reaction_id}/delete/')
def delete_message_reaction(request, message_reaction_id):
    """Delete a specific message_reaction details"""
    message_reaction = get_object_or_404(MessageReaction, id=message_reaction_id)
    if message_reaction:
        message_reaction.delete()
        return f"Emoticon {message_reaction.id} deleted succesfully"
    return message_reaction
    