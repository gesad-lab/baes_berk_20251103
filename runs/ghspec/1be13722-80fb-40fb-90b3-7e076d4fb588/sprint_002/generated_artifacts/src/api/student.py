from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel, EmailStr
from src.models import Student  # Assuming there's a Student model defined
from src.database import get_db  # Assuming there's a method to get DB session

router = APIRouter()

class StudentResponse(BaseModel):
    name: str
    email: EmailStr

@router.get("/students", response_model=List[StudentResponse])
async def get_students(db: Session = Depends(get_db)):
    """
    Retrieve a list of all students with their emails.

    Args:
        db (Session): The database session.

    Returns:
        List[StudentResponse]: A list of students with their names and emails.
    """
    students = db.query(Student).all()  # Fetch all student records
    return students  # FastAPI will automatically convert to JSON due to response_model

# Ensure to include error handling for possible DB access issues in real scenarios

