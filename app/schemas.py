
from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional


class Post(BaseModel):
    title: str
    content: str
    published: bool = True

class CreatePost(BaseModel):
    title: str
    content: str
    published: bool =True

class UpdatePost(BaseModel):
    published: bool

class ResponsePost(BaseModel):
    id:int
    title: str
    content: str
    published: bool = True
    created_at: datetime
    class Config:
        orm_mode=True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id:int
    email: EmailStr
    created_at: datetime
    
class UserLogin(BaseModel):
    id:int
    email: EmailStr
    
    created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]=None