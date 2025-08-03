from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import api_router
from app.config import settings
from app.utils.database import init_db, create_default_admin
from app.models.database import SessionLocal

app = FastAPI(
    title="Medical BI - Business Intelligence pour Services Médicaux",
    description="Application SaaS de Business Intelligence modulaire pour les services médicaux",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")


@app.on_event("startup")
async def startup_event():
    """Initialize database and create default admin user on startup"""
    init_db()
    db = SessionLocal()
    try:
        create_default_admin(db)
    finally:
        db.close()


@app.get("/")
async def root():
    return {
        "message": "Medical BI API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}