```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session
from src.db.models import Student  # Assuming this imports the Student model
from src.db.database import get_db  # Assuming a dependency for database session

router = APIRouter()

class StudentCreate(BaseModel):
    name: str = Field(..., max_length=100)
    email: EmailStr  # Email validation using Pydantic

@router.post("/students/", response_model=Student)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """Create a new student with name and email.
    
    Args:
        student (StudentCreate): Student data containing name and email.
        db (Session): Database session dependency.

    Returns:
        Student: The created student object.

    Raises:
        HTTPException: If email is not provided or has an invalid format.
    """
    # Check if student with the same email already exists
    existing_student = db.query(Student).filter(Student.email == student.email).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_student = Student(name=student.name, email=student.email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

@router.get("/students/", response_model=List[Student])
def get_students(db: Session = Depends(get_db)):
    """Retrieve all students from the database.

    Args:
        db (Session): Database session dependency.

    Returns:
        List[Student]: A list of student objects.
    """
    return db.query(Student).all()
```