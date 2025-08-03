from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.models.procedure_type import ProcedureType
from app.models.user import User
from app.schemas.procedure_type import ProcedureTypeCreate, ProcedureTypeUpdate, ProcedureTypeResponse
from app.utils.auth import get_current_active_user

router = APIRouter()


@router.get("/", response_model=List[ProcedureTypeResponse])
def get_procedure_types(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    procedure_types = db.query(ProcedureType).offset(skip).limit(limit).all()
    return procedure_types


@router.post("/", response_model=ProcedureTypeResponse)
def create_procedure_type(
    procedure_type: ProcedureTypeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    db_procedure_type = ProcedureType(**procedure_type.dict())
    db.add(db_procedure_type)
    db.commit()
    db.refresh(db_procedure_type)
    return db_procedure_type


@router.get("/{procedure_type_id}", response_model=ProcedureTypeResponse)
def get_procedure_type(
    procedure_type_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    procedure_type = db.query(ProcedureType).filter(ProcedureType.id == procedure_type_id).first()
    if procedure_type is None:
        raise HTTPException(status_code=404, detail="Procedure type not found")
    return procedure_type


@router.put("/{procedure_type_id}", response_model=ProcedureTypeResponse)
def update_procedure_type(
    procedure_type_id: int,
    procedure_type: ProcedureTypeUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    db_procedure_type = db.query(ProcedureType).filter(ProcedureType.id == procedure_type_id).first()
    if db_procedure_type is None:
        raise HTTPException(status_code=404, detail="Procedure type not found")
    
    for field, value in procedure_type.dict(exclude_unset=True).items():
        setattr(db_procedure_type, field, value)
    
    db.commit()
    db.refresh(db_procedure_type)
    return db_procedure_type


@router.delete("/{procedure_type_id}")
def delete_procedure_type(
    procedure_type_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    db_procedure_type = db.query(ProcedureType).filter(ProcedureType.id == procedure_type_id).first()
    if db_procedure_type is None:
        raise HTTPException(status_code=404, detail="Procedure type not found")
    
    db.delete(db_procedure_type)
    db.commit()
    return {"message": "Procedure type deleted"}