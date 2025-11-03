```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from src.database import get_db  # Database session dependency
from src.models import Teacher  # Import Teacher model

router = APIRouter()


class TeacherCreate(BaseModel):
    """Request model for creating a Teacher."""
    name: str
    email: EmailStr


@router.post("/teachers", response_model=TeacherCreate, status_code=201)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """Create a new Teacher in the database.

    Args:
        teacher (TeacherCreate): The Teacher information to store.
        db (Session): The database session dependency.

    Raises:
        HTTPException: If a Teacher with the same email already exists.

    Returns:
        TeacherCreate: The created Teacher's details.
    """
    # Check if the email already exists in the database
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(status_code=400, detail={"error": {"code": "E003", "message": "Teacher with this email already exists."}})

    # Create a new Teacher instance
    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)

    return new_teacher


@router.get("/teachers/{teacher_id}", response_model=TeacherCreate)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific Teacher's details.

    Args:
        teacher_id (int): The ID of the Teacher to retrieve.
        db (Session): The database session dependency.

    Raises:
        HTTPException: If the Teacher is not found.

    Returns:
        TeacherCreate: The details of the requested Teacher.
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail={"error": {"code": "E004", "message": "Teacher not found."}})

    return teacher
```