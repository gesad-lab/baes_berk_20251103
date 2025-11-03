from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..models.teacher import Teacher
from ..database import get_db
from pydantic import BaseModel

router = APIRouter()

class TeacherCreate(BaseModel):
    name: str
    email: str

@router.post("/teachers", status_code=201)
async def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """
    Create a new teacher in the system.
    
    Args:
        teacher (TeacherCreate): The teacher data to create.
        db (Session): The database session.

    Raises:
        HTTPException: If a teacher with the provided email already exists.

    Returns:
        dict: Confirmation message about the creation of the teacher.
    """
    # Check if a teacher with the same email already exists
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(status_code=400, detail="E001: Email already associated with another teacher.")

    # Create and save the new teacher instance
    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)

    return {"message": "Teacher created successfully.", "teacher_id": new_teacher.id}

@router.get("/teachers")
async def get_teachers(db: Session = Depends(get_db)):
    """
    Retrieve all teachers from the system.
    
    Args:
        db (Session): The database session.

    Returns:
        list: A list of teachers with their names and emails.
    """
    # Query all teacher records
    teachers = db.query(Teacher).all()
    return [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]