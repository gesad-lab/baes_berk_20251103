from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import Student
from database import get_db
from schemas import StudentResponse

router = APIRouter()

@router.get("/students", response_model=List[StudentResponse])
def get_students(db: Session = next(get_db())):
    """
    Retrieve all students from the database.

    Args:
        db (Session): The database session for querying.

    Returns:
        List[StudentResponse]: A list of student objects containing their names.
    """
    try:
        students = db.query(Student).all()  # Query all student records
        return students
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while retrieving students.") from e