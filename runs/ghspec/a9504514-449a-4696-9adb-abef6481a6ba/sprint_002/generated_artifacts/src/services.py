```python
# File: src/services.py

import re
from src.models import Student
from src.database import db

def create_student(name: str, email: str) -> dict:
    """
    Create a new student with name and email.

    Parameters:
    - name (str): The name of the student.
    - email (str): The email of the student.

    Returns:
    - dict: A dictionary containing the student's name and email on success,
             or an error message on failure.
    """  
    # Validate email presence
    if not email:
        return {"error": {"code": "E001", "message": "Email field is required."}}

    # Validate email format
    if not is_valid_email(email):
        return {"error": {"code": "E002", "message": "Invalid email format."}}

    # Create and save the student in the database
    student = Student(name=name, email=email)
    db.session.add(student)
    db.session.commit()
    
    return {"name": student.name, "email": student.email}

def is_valid_email(email: str) -> bool:
    """
    Validate the email format using a simple regex.

    Parameters:
    - email (str): The email to validate.

    Returns:
    - bool: True if email is valid, otherwise False.
    """
    # Simple regex for validating email format
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(email_regex, email) is not None

def get_all_students() -> list:
    """
    Retrieve all students from the database.

    Returns:
    - list: A list of dictionaries containing the names and emails of all students.
    """
    students = Student.query.all()
    return [{"name": student.name, "email": student.email} for student in students]
```