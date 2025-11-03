```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
from src.models.student import Student  # Assuming Student is defined in this module
from src.database.db import get_db  # Database utility function to get the current session

router = APIRouter()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Validate email format

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/students", response_model=StudentResponse)
async def create_student(student: StudentCreate):
    """Create a new student with name and email."""
    # Create a new Student instance
    new_student = Student(name=student.name, email=student.email)

    # Save to the database
    db = get_db()
    db.add(new_student)
    try:
        db.commit()
        db.refresh(new_student)  # Refresh to get the newly created ID
    except Exception as e:
        db.rollback()  # Roll back the transaction on error
        raise HTTPException(status_code=400, detail=str(e))

    # Return the created student's information
    return StudentResponse(id=new_student.id, name=new_student.name, email=new_student.email)

@router.get("/students", response_model=List[StudentResponse])
async def get_students():
    """Retrieve all students."""
    db = get_db()
    students = db.query(Student).all()
    return [StudentResponse(id=student.id, name=student.name, email=student.email) for student in students]
```