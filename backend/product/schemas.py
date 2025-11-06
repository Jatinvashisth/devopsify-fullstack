from pydantic import BaseModel, EmailStr
from typing import Optional

class UserData(BaseModel):
    name: str
    email: EmailStr
    phone: float
    address: EmailStr


class DisplayUser(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True



class User(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    email : EmailStr
    password: str




class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None    