from fastapi import APIRouter
from .auth import router as auth_router
from .procedures import router as procedures_router
from .rooms import router as rooms_router
from .professionals import router as professionals_router
from .procedure_types import router as procedure_types_router
from .dashboard import router as dashboard_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["authentication"])
api_router.include_router(procedures_router, prefix="/procedures", tags=["procedures"])
api_router.include_router(rooms_router, prefix="/rooms", tags=["rooms"])
api_router.include_router(professionals_router, prefix="/professionals", tags=["professionals"])
api_router.include_router(procedure_types_router, prefix="/procedure-types", tags=["procedure-types"])
api_router.include_router(dashboard_router, prefix="/dashboard", tags=["dashboard"])