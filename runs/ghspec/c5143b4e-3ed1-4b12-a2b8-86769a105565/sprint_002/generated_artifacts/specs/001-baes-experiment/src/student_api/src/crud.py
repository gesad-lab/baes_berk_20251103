```python
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .models import Student
from .schemas import StudentCreate

def create_student(db: Session, student: StudentCreate) -> Student:
    """
    Create a new student in the database.
    
    Parameters:
    - db: SQLAlchemy session for database interaction.
    - student: An instance of StudentCreate containing student details.
    
    Returns:
    - The created Student object.
    
    Raises:
    - HTTPException: If the email field is missing or invalid.
    """
    # Validate the presence of the email
    if not student.email:
        # Raise an HTTP 400 Bad Request error with details
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": {"code": "E001", "message": "Email is required."}}
        )

    # Check if the email is valid (simple format check, can be enhanced)
    if "@" not in student.email or "." not in student.email.split("@")[-1]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": {"code": "E002", "message": "Invalid email format."}}
        )

    # Create a new Student instance
    db_student = Student(name=student.name, email=student.email)
    
    # Add the new student to the session and commit
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    
    return db_student
```