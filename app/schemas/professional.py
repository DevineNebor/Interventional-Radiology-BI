from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProfessionalBase(BaseModel):
    name: str
    role: str
    service: str


class ProfessionalCreate(ProfessionalBase):
    pass


class ProfessionalUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    service: Optional[str] = None
    is_active: Optional[bool] = None


class ProfessionalResponse(ProfessionalBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True