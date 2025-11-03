```python
# src/services.py

from sqlalchemy.exc import IntegrityError
from src.models import Student  # Assuming Student model is defined in models.py
from flask import jsonify, abort
import re

def validate_email(email: str) -> bool:
    """
    Validate the given email address.
    
    Parameters:
    - email (str): The email address to validate.

    Returns:
    - bool: True if the email address is valid, False otherwise.
    """
    if not email or not isinstance(email, str):
        return False
    # Basic email format validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def create_student(name: str, email: str) -> dict:
    """
    Create a new student record.

    Parameters:
    - name (str): The name of the student.
    - email (str): The email address of the student.

    Returns:
    - dict: The created student record.

    Raises:
    - ValueError: If the name or email is invalid.
    """
    if not name:
        raise ValueError("Name cannot be empty")
    
    if not validate_email(email):
        raise ValueError("Invalid email format")

    new_student = Student(name=name, email=email)

    try:
        # Assuming a session is available for committing the new student
        session.add(new_student)
        session.commit()
        return {'id': new_student.id, 'name': new_student.name, 'email': new_student.email}
    except IntegrityError:
        session.rollback()  # Roll back the session on error
        abort(400, description="Failed to create student record due to integrity error")

def get_students() -> list:
    """
    Get a list of all student records.

    Returns:
    - list: A list of dictionaries representing all students.
    """
    students = session.query(Student).all()
    return [{'id': student.id, 'name': student.name, 'email': student.email} for student in students]

def update_student(student_id: int, name: str, email: str) -> dict:
    """
    Update an existing student record.

    Parameters:
    - student_id (int): The ID of the student to update.
    - name (str): The new name of the student.
    - email (str): The new email address of the student.

    Returns:
    - dict: The updated student record.

    Raises:
    - ValueError: If the name or email is invalid.
    """
    if not validate_email(email):
        raise ValueError("Invalid email format")

    student = session.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        abort(404, description="Student not found")

    student.name = name
    student.email = email

    try:
        session.commit()
        return {'id': student.id, 'name': student.name, 'email': student.email}
    except IntegrityError:
        session.rollback()  # Roll back the session on error
        abort(400, description="Failed to update student record due to integrity error")
```