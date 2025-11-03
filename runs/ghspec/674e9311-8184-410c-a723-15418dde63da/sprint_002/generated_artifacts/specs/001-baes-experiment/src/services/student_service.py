```python
# services/student_service.py

from sqlalchemy.exc import IntegrityError
import re
from models.student import Student  # Assuming Student model is defined here
from your_database_module import db  # Import your database session/module

def validate_email(email: str) -> bool:
    """
    Validates the email format.
    
    :param email: Email address to validate.
    :return: True if email is valid, False otherwise.
    """
    # Basic regex for validating an email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def create_student(name: str, email: str) -> dict:
    """
    Creates a new student with a given name and email.
    
    :param name: The name of the student.
    :param email: The email address of the student.
    :return: A dictionary with the student's information if creation is successful,
             or an error message if validation fails.
    """
    # Validate email presence and format
    if not email or not validate_email(email):
        return {
            "error": {
                "code": "E001",
                "message": "Invalid or missing email format.",
                "details": {}
            }
        }, 400  # Bad Request

    # Attempt to create a new Student entity
    new_student = Student(name=name, email=email)
    try:
        db.session.add(new_student)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return {
            "error": {
                "code": "E002",
                "message": "Student with the given details already exists.",
                "details": {}
            }
        }, 409  # Conflict

    return {
        "message": "Student created successfully.",
        "student": {
            "name": new_student.name,
            "email": new_student.email
        }
    }, 201  # Created

def get_students() -> list:
    """
    Retrieves a list of all students.

    :return: A list of dictionaries containing student names and emails.
    """
    students = Student.query.all()  # Assuming Student model has a query property
    return [{
        "name": student.name,
        "email": student.email
    } for student in students]
```