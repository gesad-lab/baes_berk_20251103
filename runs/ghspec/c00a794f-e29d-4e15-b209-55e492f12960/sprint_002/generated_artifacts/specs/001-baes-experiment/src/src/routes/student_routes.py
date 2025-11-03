```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from .models import Student  # Assuming a Student model is defined in models.py
from .schemas import StudentCreate, StudentResponse  # Assuming schemas for request/response are defined
from ..database import get_db  # Assuming a database connection handler

router = APIRouter()

@router.post("/students/", response_model=StudentResponse)
async def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """
    Create a new student and store it in the database.

    Args:
        student (StudentCreate): The student details to create.
        db (Session): Database session dependency.

    Returns:
        StudentResponse: The created student details.
    """
    # Validate email format (additional checks can be introduced here)
    if not student.email:
        raise HTTPException(status_code=400, detail="E001: Missing email.")

    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@router.get("/students/", response_model=List[StudentResponse])
async def read_students(db: Session = Depends(get_db)):
    """
    Retrieve a list of all students from the database.

    Args:
        db (Session): Database session dependency.

    Returns:
        List[StudentResponse]: A list of students.
    """
    students = db.query(Student).all()
    return students
```