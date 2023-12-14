from ninja import Schema, FileEx, UploadedFile
from typing import List
from datetime import date




class AuthUserRegistrationSchema(Schema):
    email:str=None
    username:str=None    
    display_name:str=None
    phone:str=None


class AuthUserRetrievalSchema(Schema):
    id:int=None
    email:str=None
    username:str=None    
    display_name:str=None
    phone:str=None
    # image:UploadedFile
    is_active:bool=None
    is_staff:bool=None
    is_superuser:bool=None
    
    
class UserLoginSchema(Schema):
    email: str=None
    password: str=None
    
    