from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.models.professional import Professional
from app.models.user import User
from app.schemas.professional import ProfessionalCreate, ProfessionalUpdate, ProfessionalResponse
from app.utils.auth import get_current_active_user

router = APIRouter()


@router.get("/", response_model=List[ProfessionalResponse])
def get_professionals(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    professionals = db.query(Professional).offset(skip).limit(limit).all()
    return professionals


@router.post("/", response_model=ProfessionalResponse)
def create_professional(
    professional: ProfessionalCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    db_professional = Professional(**professional.dict())
    db.add(db_professional)
    db.commit()
    db.refresh(db_professional)
    return db_professional


@router.get("/{professional_id}", response_model=ProfessionalResponse)
def get_professional(
    professional_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    professional = db.query(Professional).filter(Professional.id == professional_id).first()
    if professional is None:
        raise HTTPException(status_code=404, detail="Professional not found")
    return professional


@router.put("/{professional_id}", response_model=ProfessionalResponse)
def update_professional(
    professional_id: int,
    professional: ProfessionalUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    db_professional = db.query(Professional).filter(Professional.id == professional_id).first()
    if db_professional is None:
        raise HTTPException(status_code=404, detail="Professional not found")
    
    for field, value in professional.dict(exclude_unset=True).items():
        setattr(db_professional, field, value)
    
    db.commit()
    db.refresh(db_professional)
    return db_professional


@router.delete("/{professional_id}")
def delete_professional(
    professional_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    db_professional = db.query(Professional).filter(Professional.id == professional_id).first()
    if db_professional is None:
        raise HTTPException(status_code=404, detail="Professional not found")
    
    db.delete(db_professional)
    db.commit()
    return {"message": "Professional deleted"}