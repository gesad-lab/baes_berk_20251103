```python
# src/service.py

import re
from typing import Optional
from .models import Student
from .db import db_session  # assuming you have a db session import

# Email validation regex pattern
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validate_email(email: str) -> bool:
    """Validate email format using regular expressions.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if email format is valid, False otherwise.
    """
    return re.match(EMAIL_REGEX, email) is not None

def create_student(name: str, email: str) -> Student:
    """Create a new student in the database after validating input.

    Args:
        name (str): The student's name.
        email (str): The student's email address.

    Raises:
        ValueError: If the email format is invalid.

    Returns:
        Student: The created student object.
    """
    if not validate_email(email):
        raise ValueError("Invalid email format")

    new_student = Student(name=name, email=email)
    db_session.add(new_student)
    db_session.commit()
    return new_student

def update_student(student_id: int, name: Optional[str] = None, email: Optional[str] = None) -> Student:
    """Update an existing student's information.

    Args:
        student_id (int): The ID of the student to update.
        name (Optional[str]): New name to set (if provided).
        email (Optional[str]): New email to set (if provided).

    Raises:
        ValueError: If the email format is invalid.

    Returns:
        Student: The updated student object.
    """
    student = db_session.query(Student).get(student_id)

    if not student:
        raise ValueError("Student not found")

    if email and not validate_email(email):
        raise ValueError("Invalid email format")

    if name:
        student.name = name
    if email:
        student.email = email

    db_session.commit()
    return student

def get_student(student_id: int) -> Optional[Student]:
    """Retrieve a student by ID.

    Args:
        student_id (int): The ID of the student.

    Returns:
        Optional[Student]: The student object if found, None otherwise.
    """
    return db_session.query(Student).get(student_id)

def delete_student(student_id: int) -> None:
    """Delete a student from the database.

    Args:
        student_id (int): The ID of the student to delete.
    """
    student = db_session.query(Student).get(student_id)
    if student:
        db_session.delete(student)
        db_session.commit()
```
