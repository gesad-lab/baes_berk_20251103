```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Student
from app.database import get_db
from app.schemas import StudentCreate, StudentResponse

router = APIRouter()

@router.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """
    Create a new student record.

    Parameters:
    - student: StudentCreate: Contains name and email to be added.
    - db: Session: SQLAlchemy session.

    Returns:
    - StudentResponse: The created student record.
    
    Raises:
    - HTTPException: If email or name is missing.
    """
    # Validate that email and name are provided
    if not student.name or not student.email:
        raise HTTPException(status_code=400, detail="Both name and email are required")

    # Create and save the student record
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/students", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    """
    Retrieve all student records.

    Parameters:
    - db: Session: SQLAlchemy session.

    Returns:
    - List[StudentResponse]: A list of all student records including emails.
    """
    students = db.query(Student).all()
    return students
```