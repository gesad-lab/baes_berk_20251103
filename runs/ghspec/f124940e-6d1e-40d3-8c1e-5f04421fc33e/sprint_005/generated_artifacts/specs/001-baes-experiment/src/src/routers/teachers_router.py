from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List
from ..models import Teacher
from ..database import get_db  # Assuming a function to get DB session

router = APIRouter()

class TeacherCreate(BaseModel):
    name: str
    email: str

@router.post("/teachers", response_model=TeacherCreate)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """
    Create a new teacher in the database.

    Parameters:
    - teacher: TeacherCreate containing the teacher's name and email.
    - db: Database session obtained via dependency injection.

    Returns:
    - The newly created Teacher object.
    """
    # Check if the email is already registered
    db_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if db_teacher:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new Teacher instance
    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    db.commit()  # Commit to save the new teacher
    db.refresh(new_teacher)  # Refresh to get the new instance's data
    return new_teacher

@router.get("/teachers/{teacher_id}", response_model=TeacherCreate)
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a teacher by their ID.

    Parameters:
    - teacher_id: ID of the teacher to retrieve.
    - db: Database session obtained via dependency injection.

    Returns:
    - The Teacher object if found.
    
    Raises HTTPException if teacher not found.
    """
    # Query the database for the teacher
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@router.get("/teachers", response_model=List[TeacherCreate])
def get_teachers(db: Session = Depends(get_db)):
    """
    Retrieve a list of all teachers in the database.

    Parameters:
    - db: Database session obtained via dependency injection.

    Returns:
    - A list of Teacher objects.
    """
    return db.query(Teacher).all()  # Return all teachers from the database