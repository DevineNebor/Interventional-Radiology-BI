from typing import Dict, List
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, and_
from app.models.database import get_db
from app.models.procedure import Procedure
from app.models.user import User
from app.utils.auth import get_current_active_user

router = APIRouter()


@router.get("/kpi")
def get_kpi(
    start_date: datetime = Query(default=None),
    end_date: datetime = Query(default=None),
    service: str = Query(default=None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get KPI data for dashboard"""
    
    # Default to last 30 days if no dates provided
    if not start_date:
        start_date = datetime.now() - timedelta(days=30)
    if not end_date:
        end_date = datetime.now()
    
    # Build query filters
    filters = [
        Procedure.start_time >= start_date,
        Procedure.start_time <= end_date
    ]
    
    # Get total procedures
    total_procedures = db.query(func.count(Procedure.id)).filter(*filters).scalar()
    
    # Get total duration
    total_duration = db.query(func.sum(Procedure.duration)).filter(*filters).scalar() or 0
    
    # Get average duration
    avg_duration = db.query(func.avg(Procedure.duration)).filter(*filters).scalar() or 0
    
    # Get procedures by day
    daily_procedures = db.query(
        func.date(Procedure.start_time).label('date'),
        func.count(Procedure.id).label('count')
    ).filter(*filters).group_by(func.date(Procedure.start_time)).all()
    
    # Get procedures by type
    procedures_by_type = db.query(
        Procedure.procedure_type_id,
        func.count(Procedure.id).label('count')
    ).filter(*filters).group_by(Procedure.procedure_type_id).all()
    
    return {
        "total_procedures": total_procedures,
        "total_duration": total_duration,
        "average_duration": round(avg_duration, 2),
        "daily_procedures": [
            {"date": str(item.date), "count": item.count} 
            for item in daily_procedures
        ],
        "procedures_by_type": [
            {"procedure_type_id": item.procedure_type_id, "count": item.count}
            for item in procedures_by_type
        ]
    }


@router.get("/chart-data")
def get_chart_data(
    chart_type: str = Query(..., description="Type of chart: daily, weekly, monthly"),
    start_date: datetime = Query(default=None),
    end_date: datetime = Query(default=None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get chart data for different time periods"""
    
    if not start_date:
        start_date = datetime.now() - timedelta(days=30)
    if not end_date:
        end_date = datetime.now()
    
    filters = [
        Procedure.start_time >= start_date,
        Procedure.start_time <= end_date
    ]
    
    if chart_type == "daily":
        data = db.query(
            func.date(Procedure.start_time).label('date'),
            func.count(Procedure.id).label('count'),
            func.sum(Procedure.duration).label('total_duration')
        ).filter(*filters).group_by(func.date(Procedure.start_time)).all()
        
        return [
            {
                "date": str(item.date),
                "count": item.count,
                "total_duration": item.total_duration
            }
            for item in data
        ]
    
    elif chart_type == "weekly":
        data = db.query(
            func.strftime('%Y-%W', Procedure.start_time).label('week'),
            func.count(Procedure.id).label('count'),
            func.sum(Procedure.duration).label('total_duration')
        ).filter(*filters).group_by(func.strftime('%Y-%W', Procedure.start_time)).all()
        
        return [
            {
                "week": item.week,
                "count": item.count,
                "total_duration": item.total_duration
            }
            for item in data
        ]
    
    elif chart_type == "monthly":
        data = db.query(
            func.strftime('%Y-%m', Procedure.start_time).label('month'),
            func.count(Procedure.id).label('count'),
            func.sum(Procedure.duration).label('total_duration')
        ).filter(*filters).group_by(func.strftime('%Y-%m', Procedure.start_time)).all()
        
        return [
            {
                "month": item.month,
                "count": item.count,
                "total_duration": item.total_duration
            }
            for item in data
        ]
    
    else:
        return {"error": "Invalid chart type"}