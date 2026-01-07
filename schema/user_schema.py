from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str = Field(..., example="jdoe")
    email: EmailStr = Field(..., example="jdoe@email.com")
    first_name: str = Field(..., example="John")
    last_name: str = Field(..., example="Doe")
    role: str = Field(..., example="user")

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

    model_config = ConfigDict(from_attributes=True)
