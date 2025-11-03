```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Student  # Assuming the Student model is in the models module
from database import get_db  # Assuming a function to get the database session

router = APIRouter()

@router.post("/students", response_model=Student)
async def create_student(student: Student, db: Session = Depends(get_db)):
    """
    Create a new student in the database.
    
    Args:
        student (Student): The student data containing name.
        db (Session): The database session.

    Returns:
        Student: The created student with an auto-generated ID.

    Raises:
        HTTPException: If the name is missing.
    """
    if not student.name:
        # Raise a 400 error if the name is not provided
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Name is required."}})

    db.add(student)
    db.commit()
    db.refresh(student)
    return student


@router.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a student's details by their ID.

    Args:
        student_id (int): The ID of the student to retrieve.
        db (Session): The database session.

    Returns:
        Student: The retrieved student data.

    Raises:
        HTTPException: If the student is not found.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        # Raise a 404 error if the student is not found
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Student not found."}})

    return student
```