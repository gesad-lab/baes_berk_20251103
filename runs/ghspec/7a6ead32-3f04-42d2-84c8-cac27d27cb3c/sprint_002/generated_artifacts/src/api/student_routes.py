```python
from fastapi import APIRouter, HTTPException, Body
from models import Student, StudentCreate, StudentUpdate
from sqlalchemy.orm import Session
from database import get_db
import re

router = APIRouter()

# Email validation pattern
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validate_email(email: str) -> None:
    """Validate the email format."""
    if not re.match(EMAIL_REGEX, email):
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E002", "message": "Email format is invalid."}}
        )

@router.put("/api/v1/students/{student_id}")
async def update_student(
    student_id: int,
    student_updates: StudentUpdate,
    db: Session = Depends(get_db)
) -> Student:
    """Update an existing student's information."""
    # Validate the new email format
    validate_email(student_updates.email)

    # Fetch the student from the database
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Update student's details
    student.name = student_updates.name
    student.email = student_updates.email
    db.commit()
    db.refresh(student)
    
    return student
```