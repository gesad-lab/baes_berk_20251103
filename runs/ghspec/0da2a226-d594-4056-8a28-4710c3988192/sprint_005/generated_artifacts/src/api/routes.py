```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from database import get_db
from models import Teacher
from services.teacher_service import create_teacher, get_teachers

router = APIRouter()

# Pydantic model for request validation
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

@router.post("/teachers", response_model=Teacher)
def add_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """
    Create a new teacher record in the database.

    Parameters:
    - teacher: TeacherCreate - The teacher data containing name and email.
    - db: Session - The database session.

    Returns:
    - Teacher - The created teacher record.

    Raises:
    - HTTPException: 400 if name or email are missing or invalid.
    """
    try:
        return create_teacher(teacher.name, teacher.email, db)
    except ValueError as v:
        raise HTTPException(status_code=400, detail=str(v))

@router.get("/teachers", response_model=list[Teacher])
def list_teachers(db: Session = Depends(get_db)):
    """
    Retrieve a list of existing teachers.

    Parameters:
    - db: Session - The database session.

    Returns:
    - List[Teacher] - A list of teacher records.
    """
    try:
        return get_teachers(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Could not retrieve teachers.")
```