'''
Router for handling teacher-related API endpoints.
'''
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import TeacherCreate, TeacherResponse
from crud import create_teacher, get_teachers
from database import get_db
router = APIRouter()
@router.post("/teachers/", response_model=TeacherResponse)
def create_teacher_endpoint(teacher: TeacherCreate, db: Session = Depends(get_db)):
    return create_teacher(db=db, teacher=teacher)
@router.get("/teachers/", response_model=list[TeacherResponse])
def read_teachers(db: Session = Depends(get_db)):
    return get_teachers(db=db)