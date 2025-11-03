```python
# src/services/student_service.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.models import Student  # Import the Student model for data operations
from fastapi import HTTPException

def create_student(db: Session, name: str, email: str):
    """Create a new student record in the database.
    
    Args:
        db (Session): The database session.
        name (str): The name of the student.
        email (str): The email of the student.

    Returns:
        Student: The created student object.
    
    Raises:
        HTTPException: If the email format is invalid or a database error occurs.
    """
    if not Student.validate_email(email):
        raise HTTPException(status_code=400, detail="Invalid email format")
    
    new_student = Student(name=name, email=email)
    
    try:
        db.add(new_student)
        db.commit()
        db.refresh(new_student)  # Retrieve the created student to return
    except IntegrityError:
        db.rollback()  # Roll back the session in case of error
        raise HTTPException(status_code=400, detail="Email already exists")
    
    return new_student

def get_students(db: Session):
    """Retrieve all student records from the database.
    
    Args:
        db (Session): The database session.

    Returns:
        List[Student]: A list of student objects.
    """
    return db.query(Student).all()

def update_student_email(db: Session, student_id: int, email: str):
    """Update the email of an existing student.

    Args:
        db (Session): The database session.
        student_id (int): The ID of the student to update.
        email (str): The new email to set.

    Returns:
        Student: The updated student object.

    Raises:
        HTTPException: If the student is not found or if the email format is invalid.
    """
    if not Student.validate_email(email):
        raise HTTPException(status_code=400, detail="Invalid email format")
    
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student.email = email
    
    db.commit()
    db.refresh(student)
    return student
```