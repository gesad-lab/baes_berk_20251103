```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.models.teacher import Teacher
from src.schemas.teacher import TeacherCreate, TeacherResponse
from src.db.database import get_db

router = APIRouter()

@router.post("/teachers", response_model=TeacherResponse)
async def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """Create a new teacher record."""
    # Check for existing teacher with the same email
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(
            status_code=400,
            detail="A teacher with this email already exists."
        )
    
    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

@router.get("/teachers/{teacher_id}", response_model=TeacherResponse)
async def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """Retrieve a teacher by their ID."""
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher
```