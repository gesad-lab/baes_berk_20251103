```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from database import get_db
from models import Teacher  # Assuming the Teacher model is defined in models.py
from repository import create_teacher, get_teacher_by_id  # Assuming these functions are implemented in repository.py

app = FastAPI()

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

@app.post("/teachers/", response_model=TeacherResponse)
def create_new_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """Create a new teacher."""
    # Validate input and create a new teacher record
    new_teacher = create_teacher(db, teacher.name, teacher.email)
    return new_teacher

@app.get("/teachers/{teacher_id}", response_model=TeacherResponse)
def retrieve_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """Retrieve teacher details by ID."""
    teacher = get_teacher_by_id(db, teacher_id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher
```