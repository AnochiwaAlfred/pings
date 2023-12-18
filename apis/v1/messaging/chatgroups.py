from django.shortcuts import get_object_or_404
from ninja import File, Router, FormEx
from ninja.files import UploadedFile
from typing import List, Union
from users.models import *
from messaging.models import *
from schemas.messaging import *
from django.db.models import Q

router = Router(tags=["Chat Groups Endpoints"])




@router.get('list_all_groups/', response=List[ChatGroupRetrievalSchema])
def list_groups(request):
    """Get a list of all registered groups"""
    return ChatGroup.objects.all()


@router.get('chatgroup/{chatgroup_id}/get/', response=Union[ChatGroupRetrievalSchema, str])
def chatgroup(request, chatgroup_id):
    """Get a specific chatgroup details"""
    chatgroup = get_object_or_404(ChatGroup, id=chatgroup_id)
    return chatgroup
    

@router.get('chatgroup/{chatgroup_id}/get_group_picture/')
def get_chatgroup_group_picture(request, chatgroup_id):
    """Get a registered chatgroups by ID"""
    return get_object_or_404(ChatGroup, id=chatgroup_id).group_picture.url
    
    
@router.post('chatgroup/add', response=ChatGroupRetrievalSchema)
def create_chatgroup(request, chatGroupData:ChatGroupRegistrationSchema=FormEx(None)):
    """Create a new chatgroup"""
    chatgroup = ChatGroup.objects.create(**chatGroupData.dict())
    return chatgroup

@router.post('chatgroup/{chatgroup_id}/update_group_picture', response=Union[ChatGroupRetrievalSchema, str])
def update_chatgroup_group_picture(request, chatgroup_id:str, group_picture:UploadedFile=FileEx(None)):
    """
    Update chatgroup: Could be used to update the chatgroup group_picture.
    """
    chatgroup = get_object_or_404(ChatGroup, id=chatgroup_id)
    if chatgroup:
        if group_picture!=None:
            chatgroup.group_picture=group_picture
            chatgroup.save()
    return chatgroup

@router.post('chatgroup/{chatgroup_id}/update_details', response=Union[ChatGroupRetrievalSchema, str])
def update_chatgroup_details(request, chatgroup_id:str, chatGroupData:ChatGroupRegistrationSchema=FormEx(None)):
    """
    Update chatgroup: Could be used to update the chatgroup name or description.
    """
    chatgroup = get_object_or_404(ChatGroup, id=chatgroup_id)
    if chatgroup:
        for key, value in chatGroupData.dict().items():
            if value!=None:
                setattr(chatgroup, key, value)
                chatgroup.save()
    return chatgroup


@router.post('chatgroup/{chatgroup_id}/add_members', response=Union[ChatGroupRetrievalSchema, str])
def add_members_to_chatgroup(request, chatgroup_id:str, members_id:List[str]):
    """
    Add members to chatgroup
    """
    chatgroup = get_object_or_404(ChatGroup, id=chatgroup_id)
    if chatgroup:
        for id in members_id:
            user = CustomUser.objects.filter(id=id)
            if user.exists():
                chatgroup.members.add(user[0])
    return chatgroup

@router.post('chatgroup/{chatgroup_id}/remove_members', response=Union[ChatGroupRetrievalSchema, str])
def remove_members_to_chatgroup(request, chatgroup_id:str, members_id:List[str]):
    """
    Remove members from chatgroup
    """
    chatgroup = get_object_or_404(ChatGroup, id=chatgroup_id)
    if chatgroup:
        for id in members_id:
            user = CustomUser.objects.filter(id=id)
            if user.exists():
                chatgroup.members.remove(user[0])
    return chatgroup


@router.delete('chatgroup/{chatgroup_id}/delete/')
def delete_chatgroup(request, chatgroup_id):
    """Delete a specific chatgroup"""
    chatgroup = get_object_or_404(ChatGroup, id=chatgroup_id)
    if chatgroup:
        chatgroup.delete()
        return "ChatGroup {chatgroup.id} deleted successfully"
    return chatgroup

