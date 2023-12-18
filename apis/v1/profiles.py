from django.shortcuts import get_object_or_404
from ninja import Router, FormEx
from typing import List, Union
from notifications.models.notifications import Notification
from plugins.hasher import hasherGenerator
from users.models import *
from profiles.models import *
from schemas.profiles import *
from django.db.models import Q


router = Router(tags=["Profiles Endpoints"])

@router.get('list_all_friendship/', response=List[FriendshipRetrievalSchema])
def list_friendships(request):
    """List all friendships"""
    return Friendship.objects.all()

@router.get('friendship/{friendship_id}/get/', response=Union[FriendshipRetrievalSchema, str])
def get_friendship(request, friendship_id):
    """Get a specific friend detail"""
    try:
        friendship = get_object_or_404(Friendship, id=friendship_id)
        return friendship
    except Exception as e:
        return str(e)

@router.get('friendship/{user_id}/friends/', response=List[FriendshipRetrievalSchema])
def get_user_friends(request, user_id):
    """List all friends associated with a user"""
    friends = Friendship.objects.filter(Q(user_id=user_id) | Q(friend_id=user_id), is_accepted=True)
    return friends

@router.post('friendship/friends/add/', response=Union[FriendshipRetrievalSchema, str])
def send_friend_request(request, friendData:FriendshipRegistrationSchema=FormEx(None)):
    """Create a new friend object in the database,, and sends a friend request to the user"""
    checkFriends = Friendship.objects.filter(user_id=friendData.dict().get("user_id"), friend_id=friendData.dict().get("friend_id"))
    if checkFriends.exists():
        return checkFriends[0]
    else:
        friend = Friendship.objects.create(**friendData)
        content = f"{friend.user} sent you a friend request"
        notification = Notification.objects.create(user_id=friendData.dict().get("friend_id"), content=content)
        return friend
    
@router.patch('friendship/{friendship_id}/accept_request', response=Union[FriendshipRetrievalSchema, str])
def accept_friend_request(request, friendship_id):
    """Accept a friend request by updating the status of the friend object to accepted"""
    friendship = get_object_or_404(Friendship, id=friendship_id)
    if friendship:
        friendship.is_accepted=True
        friendship.save()
    return friendship

@router.patch('friendship/{friendship_id}/reject_request')
def reject_friend_request(request, friendship_id):
    """Reject a friend request by deleting the friend object"""
    friendship = get_object_or_404(Friendship, id=friendship_id)
    if friendship:
        friendship.delete()
    return f"Friendship {friendship.id} deleted"