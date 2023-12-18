from django.shortcuts import get_object_or_404
from ninja import File, Router, FormEx
from ninja.files import UploadedFile
from typing import List, Union
from users.models import *
from messaging.models import *
from schemas.messaging import *
from django.db.models import Q


router = Router(tags=["Custom Emoticons Endpoints"])

@router.get('list_all_custom_emoticons/', response=List[CustomEmoticonRetrievalSchema])
def list_custom_emoticons(request):
    """Get a list of all registered custom_emoticons"""
    return CustomEmoticon.objects.all()


@router.get('custom_emoticon/{custom_emoticon_id}/get/', response=Union[CustomEmoticonRetrievalSchema, str])
def custom_emoticon(request, custom_emoticon_id):
    """Get a specific custom_emoticon details"""
    custom_emoticon = get_object_or_404(CustomEmoticon, id=custom_emoticon_id)
    return CustomEmoticonRetrievalSchema(
        id=custom_emoticon.id,
        user=custom_emoticon.user,
        shortcut=custom_emoticon.shortcut,
        image=custom_emoticon.image.url
    )
    

@router.post('custom_emoticon/add', response=CustomEmoticonRetrievalSchema)
def create_custom_emoticon(request, customEmoticonData:CustomEmoticonRegistrationSchema, image:UploadedFile=FileEx(None)):
    """Create a new custom_emoticon"""
    custom_emoticon = CustomEmoticon.objects.create(**customEmoticonData.dict())
    custom_emoticon.image=image
    custom_emoticon.save()
    return CustomEmoticonRetrievalSchema(
        id=custom_emoticon.id,
        user=custom_emoticon.user,
        shortcut=custom_emoticon.shortcut,
        image=custom_emoticon.image.url
    )



@router.delete('custom_emoticon/{custom_emoticon_id}/delete/')
def delete_custom_emoticon(request, custom_emoticon_id):
    """Delete a specific custom_emoticon details"""
    custom_emoticon = get_object_or_404(CustomEmoticon, id=custom_emoticon_id)
    if custom_emoticon:
        custom_emoticon.delete()
        return f"Emoticon {custom_emoticon.id} deleted succesfully"
    return CustomEmoticonRetrievalSchema(
        id=custom_emoticon.id,
        user=custom_emoticon.user,
        shortcut=custom_emoticon.shortcut,
        image=custom_emoticon.image.url
    )
    