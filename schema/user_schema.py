from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    role: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = None
    active: Optional[bool] = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    active: bool
    created_at: datetime

    class Config:
        orm_mode = True
