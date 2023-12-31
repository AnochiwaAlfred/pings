from django.shortcuts import get_object_or_404
from ninja import File, Router, FormEx
from ninja.files import UploadedFile
from typing import List, Union
from users.models import *
from schemas.auth import *



router = Router(tags=["Users Endpoints"])

@router.get('list_users/', response=List[AuthUserRetrievalSchema])
def list_users(request):
    """Get a list of all registered users"""
    return CustomUser.objects.filter(is_superuser=False)

@router.get('user/{user_id}/get/', response=AuthUserRetrievalSchema)
def get_user(request, user_id):
    """Get a registered users by ID"""
    return get_object_or_404(CustomUser, id=user_id)

@router.get('user/{user_id}/get_image/')
def get_user_image(request, user_id):
    """Get a registered users by ID"""
    return get_object_or_404(CustomUser, id=user_id).image.url

@router.post('user/add/', response=Union[AuthUserRetrievalSchema, str])
def add_user(request, password:str, userData:AuthUserRegistrationSchema=FormEx(...), image:UploadedFile=FileEx(None)):
    """
    Create new user
    """    
    try:
        user = CustomUser.objects.create(**userData.dict())
        if user:
            user.set_password(password)
            user.image=image
            user.save()
        return user
    except Exception as e:
        return str(e)
    
    
@router.patch('user/{user_id}/update', response=Union[AuthUserRetrievalSchema, str])
def update_user(request, user_id:str, password:str=None, display_name:str=None):
    """
    Update User: Could be used to update the users password, display_name or image.
    If all three will not be updated, ignore the rest in the request
    """
    user = get_object_or_404(CustomUser, id=user_id)
    if user:
        if password != None:
            user.set_password(password)
            user.save()
        if display_name!=None:
            user.display_name=display_name
            user.save()
    return user

@router.post('user/{user_id}/update_image', response=Union[AuthUserRetrievalSchema, str])
def update_user_image(request, user_id:str, image:UploadedFile=FileEx(...)):
    """
    Update User: Could be used to update the user image.
    """
    user = get_object_or_404(CustomUser, id=user_id)
    if user:
        if image!=None:
            user.image=image
            user.save()
    return user

@router.delete('user/{user_id}/delete')
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if user:
        user.delete()
        return f"User {user.username} deleted successfully"
    return user

