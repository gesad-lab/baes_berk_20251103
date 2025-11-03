```python
# File: services/teacher_service.py

from sqlalchemy.orm import Session
from models import Teacher  # Assume Teacher model is already defined
from fastapi import HTTPException, status

def validate_teacher_input(name: str, email: str) -> None:
    """
    Validates input for creating a Teacher record.
    
    Parameters:
        name (str): The name of the teacher. Must not be empty.
        email (str): The email of the teacher. Must be a valid email format and unique.

    Raises:
        HTTPException: If validation fails, raises an HTTPException with a 400 status code and an error message.
    """
    if not name or not email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "E001", "message": "Name and email are required fields."}
        )
    
    # Additional validation for email format can be implemented here
    # For example: if not is_valid_email(email): ...

def create_teacher(db: Session, name: str, email: str) -> Teacher:
    """
    Creates a new Teacher record in the database.

    Parameters:
        db (Session): The database session.
        name (str): The name of the teacher.
        email (str): The email of the teacher.

    Returns:
        Teacher: The created Teacher record.

    Raises:
        HTTPException: If input validation fails or if the email is not unique.
    """
    # Validate input
    validate_teacher_input(name, email)

    # Check for existing teacher with the same email
    existing_teacher = db.query(Teacher).filter(Teacher.email == email).first()
    if existing_teacher:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "E002", "message": "Email must be unique."}
        )
    
    # Create new teacher record
    new_teacher = Teacher(name=name, email=email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)

    return new_teacher

def get_teacher(db: Session, teacher_id: int) -> Teacher:
    """
    Retrieves a Teacher record from the database by ID.

    Parameters:
        db (Session): The database session.
        teacher_id (int): The ID of the teacher to retrieve.

    Returns:
        Teacher: The Teacher record.

    Raises:
        HTTPException: If the teacher is not found.
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"code": "E003", "message": "Teacher not found."}
        )
    
    return teacher
```