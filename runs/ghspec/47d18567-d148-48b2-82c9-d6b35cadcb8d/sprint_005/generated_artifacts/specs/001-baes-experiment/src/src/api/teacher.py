```python
from fastapi import APIRouter, HTTPException, Status
from pydantic import BaseModel, EmailStr
from typing import List
from src.db.models import Teacher  # Assuming Teacher model exists
from src.db.database import get_db  # Presuming a get_db function exists for database sessions
from sqlalchemy.orm import Session

router = APIRouter()

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/teachers", response_model=TeacherResponse, status_code=Status.HTTP_201_CREATED)
async def create_teacher(teacher: TeacherCreate, db: Session = next(get_db())):
    """
    Create a new teacher entry in the database.

    Parameters:
    - teacher: TeacherCreate model instance with name and email.

    Returns:
    - A TeacherResponse instance containing the created teacher data.
    
    Raises:
    - HTTPException: If name or email is missing or if email is invalid.
    """
    # Check if the name or email is empty
    if not teacher.name or not teacher.email:
        raise HTTPException(
            status_code=Status.HTTP_400_BAD_REQUEST,
            detail={"error": {"code": "E001", "message": "Name and email are required."}}
        )

    # Create a new teacher instance and add to the session
    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    
    # Commit the session to save the new teacher
    db.commit()
    db.refresh(new_teacher)

    return new_teacher

@router.get("/teachers", response_model=List[TeacherResponse], status_code=Status.HTTP_200_OK)
async def retrieve_teachers(db: Session = next(get_db())):
    """
    Retrieve a list of all teachers from the database.

    Returns:
    - A list of TeacherResponse instances containing all teacher data.
    """
    teachers = db.query(Teacher).all()  # Retrieve all teachers from the database
    return teachers
```