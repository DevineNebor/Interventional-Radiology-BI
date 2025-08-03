from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProcedureBase(BaseModel):
    procedure_type_id: int
    room_id: int
    professional_id: int
    duration: float
    start_time: datetime
    end_time: datetime
    adverse_event: Optional[str] = None
    notes: Optional[str] = None


class ProcedureCreate(ProcedureBase):
    pass


class ProcedureUpdate(BaseModel):
    procedure_type_id: Optional[int] = None
    room_id: Optional[int] = None
    professional_id: Optional[int] = None
    duration: Optional[float] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    adverse_event: Optional[str] = None
    notes: Optional[str] = None


class ProcedureResponse(ProcedureBase):
    id: int
    created_by: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True