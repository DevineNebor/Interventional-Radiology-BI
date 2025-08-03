from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.models.procedure import Procedure
from app.models.user import User
from app.schemas.procedure import ProcedureCreate, ProcedureUpdate, ProcedureResponse
from app.utils.auth import get_current_active_user

router = APIRouter()


@router.get("/", response_model=List[ProcedureResponse])
def get_procedures(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    procedures = db.query(Procedure).offset(skip).limit(limit).all()
    return procedures


@router.post("/", response_model=ProcedureResponse)
def create_procedure(
    procedure: ProcedureCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    db_procedure = Procedure(**procedure.dict(), created_by=current_user.id)
    db.add(db_procedure)
    db.commit()
    db.refresh(db_procedure)
    return db_procedure


@router.get("/{procedure_id}", response_model=ProcedureResponse)
def get_procedure(
    procedure_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    procedure = db.query(Procedure).filter(Procedure.id == procedure_id).first()
    if procedure is None:
        raise HTTPException(status_code=404, detail="Procedure not found")
    return procedure


@router.put("/{procedure_id}", response_model=ProcedureResponse)
def update_procedure(
    procedure_id: int,
    procedure: ProcedureUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    db_procedure = db.query(Procedure).filter(Procedure.id == procedure_id).first()
    if db_procedure is None:
        raise HTTPException(status_code=404, detail="Procedure not found")
    
    for field, value in procedure.dict(exclude_unset=True).items():
        setattr(db_procedure, field, value)
    
    db.commit()
    db.refresh(db_procedure)
    return db_procedure


@router.delete("/{procedure_id}")
def delete_procedure(
    procedure_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    db_procedure = db.query(Procedure).filter(Procedure.id == procedure_id).first()
    if db_procedure is None:
        raise HTTPException(status_code=404, detail="Procedure not found")
    
    db.delete(db_procedure)
    db.commit()
    return {"message": "Procedure deleted"}