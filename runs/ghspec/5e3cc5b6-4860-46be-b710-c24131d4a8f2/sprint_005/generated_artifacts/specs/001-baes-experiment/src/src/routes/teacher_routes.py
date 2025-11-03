```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database.database import get_db
from src.models.teacher import Teacher
from src.schemas.teacher_schema import TeacherCreate, TeacherResponse

router = APIRouter()

@router.post("/teachers", response_model=TeacherResponse, status_code=201)
async def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """
    Create a new Teacher entity.

    - **name**: Required string, the name of the Teacher.
    - **email**: Required string, the email of the Teacher.
    
    Returns the created Teacher's details on success.
    Raises HTTP 400 if validation fails.
    """
    # Check if a teacher with the same email already exists
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(status_code=400, detail="Teacher with this email already exists.")

    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

@router.get("/teachers/{id}", response_model=TeacherResponse)
async def get_teacher(id: int, db: Session = Depends(get_db)):
    """
    Retrieve a Teacher entity by its ID.

    - **id**: Required integer, the ID of the Teacher.
    
    Returns the Teacher's details if found.
    Raises HTTP 404 if the Teacher does not exist.
    """
    teacher = db.query(Teacher).filter(Teacher.id == id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found.")
    return teacher
```