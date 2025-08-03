from sqlalchemy.orm import Session
from app.models import Base, engine, User
from app.utils.auth import get_password_hash


def init_db():
    """Initialize database with tables and default data"""
    Base.metadata.create_all(bind=engine)


def create_default_admin(db: Session):
    """Create default admin user if not exists"""
    admin = db.query(User).filter(User.email == "admin@medical-bi.com").first()
    if not admin:
        admin_user = User(
            email="admin@medical-bi.com",
            password=get_password_hash("admin123"),
            role="admin"
        )
        db.add(admin_user)
        db.commit()
        print("Default admin user created: admin@medical-bi.com / admin123")