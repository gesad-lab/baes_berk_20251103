```python
from fastapi import FastAPI, HTTPException, Path, Body
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from your_application.database import get_db, SessionLocal
from your_application.models import Student  # Assuming the Student model exists
from typing import Optional

app = FastAPI()

class StudentUpdate(BaseModel):
    email: EmailStr

@app.put("/students/{id}", response_model=Student)
def update_student_email(
    id: int = Path(..., title="The ID of the student to update"),
    student_update: StudentUpdate = Body(...),
    db: Session = next(get_db())
) -> Student:
    """
    Update the email of an existing student.

    - **id**: The ID of the student to update.
    - **student_update**: A StudentUpdate model instance containing the new email.

    Returns the updated student record.
    """
    # Retrieve the student from the database
    student = db.query(Student).filter(Student.id == id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Update the student's email
    student.email = student_update.email
    db.commit()
    db.refresh(student)
    
    return student
```