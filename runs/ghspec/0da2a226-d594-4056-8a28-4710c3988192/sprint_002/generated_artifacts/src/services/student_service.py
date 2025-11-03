```python
# src/services/student_service.py

from sqlalchemy.orm import Session
from models import Student

def create_student(name: str, email: str, db: Session):
    """Create a new student with a name and an email."""
    if not email:
        raise ValueError("Email is a required field.")  # Ensure email is provided

    new_student = Student(name=name, email=email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def get_student(student_id: int, db: Session):
    """Retrieve a student by their ID, including their email."""
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise ValueError(f"Student with ID {student_id} not found.")
    return student

def update_student(student_id: int, new_email: str, db: Session):
    """Update the email of an existing student."""
    if not new_email:
        raise ValueError("New email is a required field.")  # Ensure new email is provided

    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise ValueError(f"Student with ID {student_id} not found.")

    # Update student's email
    student.email = new_email
    db.commit()
    return student
```