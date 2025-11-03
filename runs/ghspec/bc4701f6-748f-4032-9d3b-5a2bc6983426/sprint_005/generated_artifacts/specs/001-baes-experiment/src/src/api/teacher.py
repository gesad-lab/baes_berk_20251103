```python
from fastapi import APIRouter, HTTPException, Depends, Body
from pydantic import BaseModel, EmailStr
from typing import Optional
from src.models.teacher import Teacher  # Assuming the Teacher model exists
from src.database import get_db  # Assuming a database session dependency
from sqlalchemy.orm import Session

router = APIRouter()

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

@router.post("/teachers", response_model=TeacherResponse, status_code=201)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """
    Create a new Teacher record in the database.

    :param teacher: TeacherCreate model containing name and email.
    :param db: Database session dependency.
    :return: The created Teacher's details.
    """
    # Check if required fields are provided; FastAPI automatically validates this
    if not teacher.name or not teacher.email:
        raise HTTPException(status_code=400, detail="Missing required fields: name or email.")
    
    # Create the teacher in the database
    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    
    try:
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)
    except Exception as e:
        db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=500, detail="Failed to create teacher.")

    return TeacherResponse(id=new_teacher.id, name=new_teacher.name, email=new_teacher.email)

@router.get("/teachers/{teacher_id}", response_model=TeacherResponse)
def retrieve_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a Teacher's information by ID.

    :param teacher_id: The unique ID of the teacher.
    :param db: Database session dependency.
    :return: The Teacher's details if found.
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found.")
    
    return TeacherResponse(id=teacher.id, name=teacher.name, email=teacher.email)

# Note: Ensure to include the router in your main application instance.
```