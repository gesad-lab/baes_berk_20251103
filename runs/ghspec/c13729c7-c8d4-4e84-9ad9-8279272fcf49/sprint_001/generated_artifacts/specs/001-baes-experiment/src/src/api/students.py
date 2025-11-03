from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, constr
from sqlalchemy.orm import Session
from ..models.student import Student
from ..database.session import get_db

router = APIRouter()

class StudentCreate(BaseModel):
    name: constr(strip_whitespace=True)  # Required name field, trimmed for whitespace

@router.post("/students", response_model=Student)
def create_student(student: StudentCreate, db: Session = next(get_db())):
    """
    Create a new student.

    Args:
        student (StudentCreate): The student data to be created.
        db (Session): The database session.

    Returns:
        Student: The created student object.

    Raises:
        HTTPException: If name is missing or empty.
    """
    # Validate the name field for presence
    if not student.name:
        raise HTTPException(
            status_code=400,
            detail={
                "error": {
                    "code": "E001",
                    "message": "Name is required.",
                    "details": {"field": "name"}
                }
            }
        )

    # Create a new student instance
    new_student = Student(name=student.name)

    # Add the new student to the session and commit
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

