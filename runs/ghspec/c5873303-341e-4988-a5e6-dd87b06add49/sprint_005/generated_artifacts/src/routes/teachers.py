```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from src.models import Teacher
from src.database import get_db

router = APIRouter()

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

@router.post("/teachers", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """
    Create a new teacher in the system.

    Args:
        teacher (TeacherCreate): The teacher data to create.
        db (Session, optional): The database session. Defaults to getting a session.

    Returns:
        TeacherResponse: The created teacher's details.

    Raises:
        HTTPException: If the email is already in use or other validation issues occur.
    """
    # Check if a teacher with the same email already exists
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(status_code=400, detail="Email already in use")

    # Create a new teacher instance
    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)

    return TeacherResponse(id=new_teacher.id, name=new_teacher.name, email=new_teacher.email)

@router.get("/teachers", response_model=list[TeacherResponse])
def get_teachers(db: Session = Depends(get_db)):
    """
    Retrieve the list of all teachers in the system.

    Args:
        db (Session, optional): The database session. Defaults to getting a session.

    Returns:
        list[TeacherResponse]: A list of teachers.
    """
    teachers = db.query(Teacher).all()
    return [TeacherResponse(id=teacher.id, name=teacher.name, email=teacher.email) for teacher in teachers]
```