```python
# src/services/teacher_service.py
from flask import abort
from src.models.teacher import Teacher  # Importing the Teacher model
from app import db  # Importing the database instance

def create_teacher(name: str, email: str) -> Teacher:
    """Create a new teacher with a name and an email.

    Args:
        name (str): The name of the teacher.
        email (str): The email address of the teacher.

    Returns:
        Teacher: The created Teacher instance.

    Raises:
        ValueError: If name or email is invalid.
    """
    validate_teacher_input(name, email)  # Validate input before proceeding

    teacher = Teacher(name=name, email=email)
    db.session.add(teacher)
    
    try:
        db.session.commit()  # Save the record to the database
    except Exception as e:
        db.session.rollback()  # Rollback in case of an error
        abort(500, description="An error occurred while creating a teacher.")  # Handle error gracefully
    
    return teacher

def list_teachers() -> list:
    """Retrieve a list of all teachers.

    Returns:
        List[Teacher]: A list of all Teacher instances.
    """
    teachers = Teacher.query.all()  # Query all teachers
    return teachers

def validate_teacher_input(name: str, email: str) -> None:
    """Validate the input for creating a teacher.

    Args:
        name (str): The name of the teacher.
        email (str): The email address of the teacher.

    Raises:
        ValueError: If name or email is invalid or missing.
    """
    if not name or not isinstance(name, str):
        raise ValueError("Invalid name provided. It must be a non-empty string.")
    
    if not email or not isinstance(email, str) or "@" not in email:
        raise ValueError("Invalid email provided. It must be a valid email address.")
```