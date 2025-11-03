from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..models import Teacher
from ..schemas import TeacherResponse, TeacherCreate
from ..database import get_db

router = APIRouter()

@router.get("/teachers/{teacher_id}", response_model=TeacherResponse)
async def get_teacher(teacher_id: int, db: Session = next(get_db())):
    """
    Retrieve a specific teacher by their unique ID.
    
    Args:
    - teacher_id (int): The ID of the teacher to retrieve.
    - db (Session): The database session.
    
    Returns:
    - TeacherResponse: The details of the teacher.
    
    Raises:
    - HTTPException: If the teacher is not found (404).
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found.")
    return teacher