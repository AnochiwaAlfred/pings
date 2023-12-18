import json
import uuid
from ninja import Schema, File
from typing import List
from datetime import datetime
from schemas.auth import *


class ChatGroupRegistrationSchema(Schema):
    name:str=None
    description:str=None


class ChatGroupRetrievalSchema(Schema):
    id:uuid.UUID=None
    name:str=None
    description:str=None
    members:List[AuthUserRetrievalSchema]=None
    # group_picture:str=None
    
    
class CustomEmoticonRegistrationSchema(Schema):
    user_id:str=None
    shortcut:str=None


class CustomEmoticonRetrievalSchema(Schema):
    id:uuid.UUID=None
    user:AuthUserRetrievalSchema=None
    shortcut:str=None
    image:str=None
    
    
class GroupMessageRegistrationSchema(Schema):
    group_id:str=None
    sender_id:str=None
    content:str=None


class GroupMessageRetrievalSchema(Schema):
    id:uuid.UUID=None
    group:ChatGroupRetrievalSchema=None
    sender:AuthUserRetrievalSchema=None
    content:str=None
    timestamp:datetime=None
    
    
class MessageRegistrationSchema(Schema):
    sender_id:str=None
    receiver_id:str=None
    content:str=None


class MessageRetrievalSchema(Schema):
    id:uuid.UUID=None
    sender:AuthUserRetrievalSchema=None
    receiver:AuthUserRetrievalSchema=None
    content:str=None
    timestamp:datetime=None
    is_read:bool=None
    image:str=None
    video:str=None
    file:str=None
    
    
class MessageReactionRegistrationSchema(Schema):
    message_id:str=None
    user_id:str=None
    emoji:str=None


class MessageReactionRetrievalSchema(Schema):
    id:uuid.UUID=None
    message:MessageRetrievalSchema=None
    user:AuthUserRetrievalSchema=None
    emoji:str=None
    
    
class PollOptionRegistrationSchema(Schema):
    context:str=None


class PollOptionRetrievalSchema(Schema):
    id:uuid.UUID=None
    context:str=None
    
    
class PollRegistrationSchema(Schema):
    question:str=None
    creator_id:str=None


class PollRetrievalSchema(Schema):
    id:uuid.UUID=None
    question:str=None
    creator:AuthUserRetrievalSchema=None
    options:List[PollOptionRetrievalSchema]=None
    
    
class PollVoteRegistrationSchema(Schema):
    user_id:str=None
    poll_id:str=None
    selected_option_id:str=None


class PollVoteRetrievalSchema(Schema):
    id:uuid.UUID=None
    user:AuthUserRetrievalSchema=None
    poll:PollRetrievalSchema=None
    selected_option:PollOptionRetrievalSchema=None
    
    
