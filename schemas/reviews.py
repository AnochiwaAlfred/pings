import uuid
from ninja import Schema, File
from typing import List
from datetime import date
from schemas.auth import AuthUserRetrievalSchema
from schemas.messaging import MessageRetrievalSchema



class ReportRegistrationSchema(Schema):
    user_id:str=None
    message_id:str=None
    reason:str=None


class ReportRetrievalSchema(Schema):
    id:uuid.UUID=None
    user:AuthUserRetrievalSchema=None
    message:MessageRetrievalSchema=None
    reason:str=None


class UserBlockRegistrationSchema(Schema):
    user_id:str=None
    blocked_user_id:str=None


class UserBlockRetrievalSchema(Schema):
    id:uuid.UUID=None
    user:AuthUserRetrievalSchema=None
    blocked_user:AuthUserRetrievalSchema=None