from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class RoomBase(BaseModel):
    name: str
    service: str


class RoomCreate(RoomBase):
    pass


class RoomUpdate(BaseModel):
    name: Optional[str] = None
    service: Optional[str] = None
    is_active: Optional[bool] = None


class RoomResponse(RoomBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True