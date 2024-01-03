import uuid
import json
from ninja import Schema, File
from typing import List
from datetime import datetime
from schemas.auth import *




class UserProfileRegistrationSchema(Schema):
    user_id:str=None
    bio:str=None


class UserProfileRetrievalSchema(Schema):
    id:uuid.UUID=None
    user:AuthUserRetrievalSchema=None
    bio:str=None


class FriendshipRegistrationSchema(Schema):
    user_id:str=None
    friend_username:str=None


class FriendshipRetrievalSchema(Schema):
    id:uuid.UUID=None
    user:AuthUserRetrievalSchema=None
    friend:AuthUserRetrievalSchema=None
    is_accepted:bool=None
    

class UserSettingRegistrationSchema(Schema):
    user_id:str=None
    theme:str=None
    notification_preferences:str=None


class UserSettingRetrievalSchema(Schema):
    id:uuid.UUID=None
    user:AuthUserRetrievalSchema=None
    theme:str=None
    notification_preferences:str=None
