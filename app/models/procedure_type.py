from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.sql import func
from .database import Base


class ProcedureType(Base):
    __tablename__ = "procedure_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    default_duration = Column(Float, nullable=False)  # durée en minutes
    service = Column(String, nullable=False)  # radiologie, cardiologie, etc.
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())