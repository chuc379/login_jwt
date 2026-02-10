from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class CreateUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class CreateUserResponse(BaseModel):
    id: UUID 
    username: str
    email: EmailStr


class ErrorCreateUserResponse(BaseModel):
    code: str
    message: str
