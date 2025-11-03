```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Student

router = APIRouter()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Automatically validates email format

@router.post("/students", response_model=StudentCreate)
def create_student(student: StudentCreate, db: Session = next(get_db())):
    """
    Create a new Student with name and email.

    Parameters:
    - student: StudentCreate model containing the name and email of the student.
    - db: Database session for operations.

    Returns:
    - The created Student.
    """
    # Check for existing student with the same email
    existing_student = db.query(Student).filter(Student.email == student.email).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Email already registered.")

    # Create new student instance
    new_student = Student(name=student.name, email=student.email)
    
    # Add to the session and commit to the database
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student  # Return the created Student


@router.get("/students/{student_id}", response_model=StudentCreate)
def get_student(student_id: int, db: Session = next(get_db())):
    """
    Retrieve a Student by ID.

    Parameters:
    - student_id: ID of the student to retrieve.
    - db: Database session for operations.

    Returns:
    - The requested Student.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return student  # Return the found student
```