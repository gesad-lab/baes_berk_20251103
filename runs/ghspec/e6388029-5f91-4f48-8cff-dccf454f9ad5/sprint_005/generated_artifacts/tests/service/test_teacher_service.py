```python
# File: src/services/teacher_service.py

from sqlalchemy.orm import Session
from src.models import Teacher
from src.schemas import TeacherCreate
from fastapi import HTTPException, status
import re

def create_teacher(teacher: TeacherCreate, db: Session) -> Teacher:
    """
    Create a new teacher record in the database.

    Args:
    - teacher: TeacherCreate schema containing name and email.
    - db: Database session.

    Returns:
    - Teacher: The created teacher record.

    Raises:
    - HTTPException: If name or email validation fails or if email already exists.
    """
    # Validate provided teacher data
    if not teacher.name or not teacher.email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Both name and email are required.")

    if not is_valid_email(teacher.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email format.")

    # Check if the email already exists
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists.")

    # Create new Teacher record
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    
    return db_teacher

def is_valid_email(email: str) -> bool:
    """
    Validate the email format using a regular expression.

    Args:
    - email: The email string to validate.

    Returns:
    - bool: True if the email is valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def get_teacher(teacher_id: int, db: Session) -> Teacher:
    """
    Retrieve a teacher record by its ID.

    Args:
    - teacher_id: The ID of the teacher to retrieve.
    - db: Database session.

    Returns:
    - Teacher: The teacher record matching the provided ID.

    Raises:
    - HTTPException: If the teacher is not found.
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found.")
    return teacher
```