from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, constr
from typing import List
from sqlalchemy.orm import Session
from src.database.db import get_db
from src.models.student import Student as StudentModel

router = APIRouter()

class StudentCreate(BaseModel):
    name: constr(min_length=1, max_length=100)  # Validation for name field

@router.post("/students/", response_model=StudentModel, status_code=201)
def create_student(student: StudentCreate, db: Session = next(get_db())):
    """
    Create a new student record in the database.

    Args:
        student (StudentCreate): The student data to create.
        db (Session): The database session.

    Returns:
        StudentModel: The created student with ID and name.

    Raises:
        HTTPException: If the name is invalid or other database errors occur.
    """
    new_student = StudentModel(name=student.name)
    
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    
    return new_student

@router.get("/students/", response_model=List[StudentModel])
def read_students(db: Session = next(get_db())):
    """
    Retrieve all students from the database.

    Args:
        db (Session): The database session.

    Returns:
        List[StudentModel]: A list of students.
    """
    return db.query(StudentModel).all()