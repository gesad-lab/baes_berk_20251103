```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, constr
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Teacher  # Assuming the Teacher model is defined in src.models

router = APIRouter()

class TeacherCreate(BaseModel):
    name: constr(min_length=1)  # Ensures name is a non-empty string
    email: EmailStr  # Validates that email is correctly formatted

@router.post("/teachers", response_model=Teacher)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    # Check for existing teacher with the same email to enforce uniqueness
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(status_code=400, detail={"error": {"code": "E002", "message": "Email already registered."}})

    # Create new Teacher instance
    new_teacher = Teacher(name=teacher.name, email=teacher.email)

    db.add(new_teacher)  # Add to session
    db.commit()  # Commit session to store changes
    db.refresh(new_teacher)  # Refresh instance to get new state with ID

    return new_teacher  # Return the created teacher
```