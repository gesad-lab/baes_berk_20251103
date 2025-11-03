```python
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field, required

# Database initialization logic would go here (e.g. creating tables)

def create_student(db: Session, name: str, email: str):
    """
    Create a new student with the provided name and email.

    Args:
        db (Session): The database session.
        name (str): The student's name.
        email (str): The student's email.

    Raises:
        HTTPException: If the student cannot be created or validation fails.

    Returns:
        Student: The created student instance.
    """
    # Simple email format validation
    if "@" not in email or "." not in email.split("@")[-1]:
        raise HTTPException(status_code=400, detail="Invalid email format.")
    
    try:
        student = Student(name=name, email=email)
        db.add(student)
        db.commit()
        db.refresh(student)
        return student
    except IntegrityError:
        db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=400, detail="Failed to create student due to integrity error.")

def get_student(db: Session, student_id: str):
    """
    Retrieve a student by ID.

    Args:
        db (Session): The database session.
        student_id (str): The student's ID.

    Returns:
        Student: The student instance.

    Raises:
        HTTPException: If the student is not found.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    return student

def update_student_email(db: Session, student_id: str, email: str):
    """
    Update the email of an existing student.

    Args:
        db (Session): The database session.
        student_id (str): The student's ID.
        email (str): The new email for the student.

    Raises:
        HTTPException: If the student is not found or if email is invalid.

    Returns:
        Student: The updated student instance.
    """
    # Simple email format validation
    if "@" not in email or "." not in email.split("@")[-1]:
        raise HTTPException(status_code=400, detail="Invalid email format.")
    
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    student.email = email
    db.commit()
    db.refresh(student)
    return student
```