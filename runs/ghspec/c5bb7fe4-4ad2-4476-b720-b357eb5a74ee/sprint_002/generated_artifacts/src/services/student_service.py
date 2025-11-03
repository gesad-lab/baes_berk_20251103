```python
# src/services/student_service.py

from src.models import Student  # Importing the existing Student model
from sqlalchemy.exc import IntegrityError
import re

def is_valid_email(email: str) -> bool:
    """Check if the provided email is in a valid format."""
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

def create_student(data):
    """
    Create a new student with the given data.

    Parameters:
    - data: dict containing student information with 'name' and 'email'.

    Returns:
    - Student object if successful, raises an error otherwise.
    """
    if not is_valid_email(data.get('email', '')):
        raise ValueError("E001: Invalid email format")

    student = Student(name=data['name'], email=data['email'])  # Modified to include email
    db.session.add(student)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise ValueError("E002: Database error occurred while creating student")

    return student

def update_student(student_id, data):
    """
    Update an existing student's information.

    Parameters:
    - student_id: The ID of the student to update.
    - data: dict containing fields to update, particularly 'email'.

    Returns:
    - The updated Student object if successful.
    """
    student = Student.query.get(student_id)
    if not student:
        raise ValueError("E003: Student not found")

    if 'email' in data:
        if not is_valid_email(data['email']):
            raise ValueError("E001: Invalid email format")
        student.email = data['email']  # Update the student's email

    db.session.commit()
    return student

def get_students():
    """
    Retrieve all students from the database.

    Returns:
    - List of Students.
    """
    return Student.query.all()
```