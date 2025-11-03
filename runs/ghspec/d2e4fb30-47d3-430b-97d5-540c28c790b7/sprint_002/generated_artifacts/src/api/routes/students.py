from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
from src.models import Student  # Assuming the Student model is located here
from src.database import get_db  # Assuming get_db is a valid database session dependency

router = APIRouter()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Use EmailStr for basic email validation

class StudentRead(BaseModel):
    id: int
    name: str
    email: str

@router.post("/students", response_model=StudentRead, status_code=201)
async def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """
    Create a new student record.

    Args:
        student (StudentCreate): The student data including name and email.
        db (Session): Database session dependency.

    Returns:
        StudentRead: The created student's details.
    
    Raises:
        HTTPException: If the email field is missing.
    """
    # Ensure that the email is provided
    if not student.email:
        raise HTTPException(status_code=400, detail="Email field is required.")
    
    # Create Student instance
    db_student = Student(name=student.name, email=student.email)
    
    # Add student to the session and commit
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    
    return db_student

@router.get("/students", response_model=List[StudentRead])
async def get_students(db: Session = Depends(get_db)):
    """
    Retrieve all registered students.

    Args:
        db (Session): Database session dependency.

    Returns:
        List[StudentRead]: A list of student records.
    """
    return db.query(Student).all()  # Return all students from the database