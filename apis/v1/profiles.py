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

@router.get('friendship/{user_id}/friends/', response=List[ContactsAuthRetrievalSchema])
def get_user_friends(request, user_id):
    """List all friends associated with a user"""
    friends=[]
    friends1 = Friendship.objects.filter(user_id=user_id, is_accepted=True)
    if friends1.exists():
        for friend in friends1:
            user1 = CustomUser.objects.get(id=friend.friend_id)
            friends.append(ContactsAuthRetrievalSchema(
                id=user1.id,
                display_name=user1.display_name,
                username=user1.username,
                image=request.build_absolute_uri(user1.image.url) if user1.image else "",
                is_online=user1.is_online,
            ))
    friends2 = Friendship.objects.filter(friend_id=user_id, is_accepted=True)
    if friends2.exists():
        for friend in friends2:
            user2 = CustomUser.objects.get(id=friend.user_id)
            friends.append(ContactsAuthRetrievalSchema(
                id=user2.id,
                display_name=user2.display_name,
                username=user2.username,
                image=request.build_absolute_uri(user2.image.url) if user2.image else "",
                is_online=user2.is_online,
            ))
    return friends

@router.get('friendship/{user_id}/friendships/', response=List[FriendshipRetrievalSchema])
def get_user_friendships(request, user_id):
    """List all friendships associated with a user"""
    friendships = Friendship.objects.filter(Q(user_id=user_id) | Q(friend_id=user_id), is_accepted=True)
    return friendships


@router.post('friendship/friends/add/', response=Union[FriendshipRetrievalSchema, str])
def send_friend_request(request, friendData:FriendshipRegistrationSchema=FormEx(None)):
    """Create a new friend object in the database,, and sends a friend request to the user"""
    friendCheck = CustomUser.objects.filter(username=friendData.dict().get("friend_username"))
    if friendCheck.exists():
        checkFriends = Friendship.objects.filter(user_id=friendData.dict().get("user_id"), friend=friendCheck[0])
        if checkFriends.exists():
            content = f"{checkFriends[0].user} sent you a friend request"
            notification = Notification.objects.create(user_id=friendData.dict().get("friend_id"), sender_id=friendData.dict().get("user_id"), content=content)
            # print(checkFriends[0])
            # return checkFriends[0]
            return f"Friend request sent to {checkFriends[0].friend.display_name}  \n#BCKEND"
        else:
            friend = Friendship.objects.create(user_id=friendData.dict().get("user_id"), friend=friendCheck[0])
            content = f"{friend.user} sent you a friend request"
            notification = Notification.objects.create(user_id=friendData.dict().get("friend_id"), sender_id=friendData.dict().get("user_id"), content=content)
            # print(f"Friend request sent to {friend.friend.display_name}")
            return f"Friend request sent to {friend.friend.display_name}  \n#BCKEND"
    else:
        # print(f"Friend with username {friendData.dict().get('friend_username')} does not exist")
        return f"Friend with username {friendData.dict().get('friend_username')} does not exist  \n#BCKEND"
        
    
@router.patch('friendship/{friendship_id}/accept_request', response=Union[FriendshipRetrievalSchema, str])
def accept_friend_request(request, friendship_id):
    """Accept a friend request by updating the status of the friend object to accepted"""
    friendship = get_object_or_404(Friendship, id=friendship_id)
    if friendship:
        friendship.is_accepted=True
        friendship.save()
        content = f"{friendship.friend} accepted your friend request"
        notification = Notification.objects.create(user=friendship.user, sender=friendship.friend, content=content)
    return friendship

@router.patch('friendship/{friendship_id}/reject_request')
def reject_friend_request(request, friendship_id):
    """Reject a friend request by deleting the friend object"""
    friendship = get_object_or_404(Friendship, id=friendship_id)
    if friendship:
        friendship.delete()
    return f"Friendship {friendship.id} deleted"