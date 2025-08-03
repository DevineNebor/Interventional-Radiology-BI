from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProcedureTypeBase(BaseModel):
    name: str
    default_duration: float
    service: str


class ProcedureTypeCreate(ProcedureTypeBase):
    pass


class ProcedureTypeUpdate(BaseModel):
    name: Optional[str] = None
    default_duration: Optional[float] = None
    service: Optional[str] = None
    is_active: Optional[bool] = None


class ProcedureTypeResponse(ProcedureTypeBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True