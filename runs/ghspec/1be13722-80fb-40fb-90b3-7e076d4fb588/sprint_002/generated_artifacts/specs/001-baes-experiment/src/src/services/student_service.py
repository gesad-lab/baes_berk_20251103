```python
import re
from typing import Optional
from src.models.student import Student  # Assuming the Student model is here
from sqlalchemy.exc import IntegrityError

def validate_email(email: str) -> bool:
    """Validates the format of the given email address.
    
    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def create_student(name: str, email: str) -> Student:
    """Creates a new student and saves it to the database.

    Args:
        name (str): The name of the student.
        email (str): The email address of the student, which must be validated.

    Returns:
        Student: The created Student object.

    Raises:
        ValueError: If the email format is invalid.
        IntegrityError: If there is a database integrity error (e.g., unique constraint).
    """
    if not validate_email(email):
        raise ValueError("Invalid email format provided.")

    student = Student(name=name, email=email)
    try:
        # Assuming db_session is the session instance for database operations
        db_session.add(student)
        db_session.commit()
        return student
    except IntegrityError:
        db_session.rollback()
        raise ValueError("Email already exists or another integrity issue occurred.")

# Other existing service methods would remain unchanged...
```