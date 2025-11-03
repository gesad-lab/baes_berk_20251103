```python
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from src.models.teacher import Teacher
from src.schemas.teacher_schemas import TeacherCreate, TeacherUpdate, TeacherResponse
from src.db.database import get_db

# Create an instance of APIRouter
router = APIRouter()

@router.post("/teachers", response_model=TeacherResponse, status_code=201)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """Create a new teacher."""
    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

@router.get("/teachers/{teacher_id}", response_model=TeacherResponse)
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """Retrieve a teacher's details by ID."""
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@router.put("/teachers/{teacher_id}", response_model=TeacherResponse)
def update_teacher(teacher_id: int, teacher: TeacherUpdate, db: Session = Depends(get_db)):
    """Update the details of a teacher."""
    existing_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not existing_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    existing_teacher.name = teacher.name
    existing_teacher.email = teacher.email
    db.commit()
    db.refresh(existing_teacher)
    return existing_teacher

@router.delete("/teachers/{teacher_id}", status_code=204)
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """Delete a teacher by ID."""
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    db.delete(teacher)
    db.commit()
    return {"detail": "Teacher deleted successfully"}
```