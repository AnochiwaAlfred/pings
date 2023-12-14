import uuid
from ninja import Schema, File
from typing import List
from schemas.auth import *
from datetime import datetime



class DeviceRegistrationSchema(Schema):
    user_id:str=None
    device_token:str=None


class DeviceRetrievalSchema(Schema):
    id:uuid.UUID=None
    user:AuthUserRetrievalSchema=None
    device_token:str=None
    
    
class NotificationRegistrationSchema(Schema):
    user_id:str=None
    content:str=None


class NotificationRetrievalSchema(Schema):
    id:uuid.UUID=None
    user:AuthUserRetrievalSchema=None
    content:str=None
    timestamp:datetime=None
    is_read:bool=None