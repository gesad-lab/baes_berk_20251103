'''
Defines the API routes for teacher management.
'''
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Teacher
from schemas import TeacherCreate, TeacherResponse
router = APIRouter()
@router.post("/teachers", response_model=TeacherResponse, status_code=201)
def create_teacher(teacher: TeacherCreate):
    with SessionLocal() as db:
        try:
            db_teacher = Teacher(name=teacher.name, email=teacher.email)
            db.add(db_teacher)
            db.commit()
            db.refresh(db_teacher)
            return db_teacher
        except Exception as e:
            db.rollback()  # Rollback in case of error
            raise HTTPException(status_code=400, detail=str(e))  # Return error response