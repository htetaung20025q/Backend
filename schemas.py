from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SavedFileCreate(BaseModel):
    file_name: str = Field(..., pattern=r".*\.txt$")
    encrypted_content: str

class SavedFileResponse(SavedFileCreate):
    id: int
    owner_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReceivedFileCreate(BaseModel):
    sender_id: int
    file_name: str = Field(..., pattern=r".*\.txt$")
    encrypted_content: str

class ReceivedFileResponse(ReceivedFileCreate):
    id: int
    receiver_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)