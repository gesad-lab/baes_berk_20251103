```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, ValidationError
from sqlalchemy.orm import Session
from src.database import get_db
from src.crud import create_teacher as crud_create_teacher
from src.models import Teacher

app = FastAPI()

# Pydantic model for validating Teacher input
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

@app.post("/teachers", response_model=Teacher)
def create_teacher(teacher: TeacherCreate, db: Session = next(get_db())):
    """
    Create a new Teacher record.
    Args:
        teacher (TeacherCreate): The validated input data containing teacher's name and email.
        db (Session): The database session to perform operations.
    Returns:
        Teacher: The newly created Teacher object.
    Raises:
        HTTPException: If there are validation issues or creation fails.
    """
    # Check for existing teacher with the same email before creation
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(status_code=400, detail="Email already registered.")

    try:
        # Create a new teacher in the database using the CRUD utility
        new_teacher = crud_create_teacher(db, teacher.name, teacher.email)
        return new_teacher  # Assuming this returns a fully populated Teacher object
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
```