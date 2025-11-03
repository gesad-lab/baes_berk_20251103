```python
# student_app/src/services/student_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.student import Student  # Import Student model
from schemas.student_schemas import StudentCreate, StudentUpdate  # Import request/response models

def create_student(db: Session, student: StudentCreate) -> Student:
    """Create a new student and save it in the database."""
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, student_id: int) -> Student:
    """Retrieve a student by ID from the database."""
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

def update_student(db: Session, student_id: int, student_update: StudentUpdate) -> Student:
    """Update an existing student's details in the database."""
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    for key, value in student_update.dict(exclude_unset=True).items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return student

def delete_student(db: Session, student_id: int) -> dict:
    """Delete a student by ID from the database."""
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()  # Commit the changes to the database

    return {"detail": "Student deleted successfully"}  # Return a confirmation message
```