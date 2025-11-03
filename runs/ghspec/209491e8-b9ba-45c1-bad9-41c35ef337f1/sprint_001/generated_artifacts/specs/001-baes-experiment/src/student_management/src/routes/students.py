from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..models import Student
from ..database import get_db
from ..schemas import StudentOut

router = APIRouter()

@router.get("/students", response_model=List[StudentOut])
def get_students(db: Session = Depends(get_db)):
    """
    Retrieve a list of all students.

    Args:
        db (Session): Database session (injected).

    Returns:
        List[StudentOut]: List of students with their names.
    """
    # Fetch all students from the database
    students = db.query(Student).all()
    
    # Check if students list is empty
    if not students:
        return []

    return students  # Returning list of StudentOut defined in schemas.py