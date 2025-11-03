```python
# src/services/teacher_service.py

from models.teacher import Teacher
from sqlalchemy.exc import IntegrityError
import re

def create_teacher(db_session, name: str, email: str) -> Teacher:
    """
    Creates a new Teacher entity and saves it to the database.

    Parameters:
    - db_session: The database session to use for the transaction.
    - name: The name of the teacher.
    - email: The email of the teacher.

    Returns:
    - The created Teacher instance.

    Raises:
    - ValueError: If the email already exists in the database.
    """
    validate_email_format(email)  # Validate the email format
    new_teacher = Teacher(name=name, email=email)
    db_session.add(new_teacher)
    try:
        db_session.commit()
        return new_teacher
    except IntegrityError:
        db_session.rollback()
        raise ValueError("Email already exists.")

def validate_email_format(email: str) -> None:
    """
    Validates the format of the provided email.

    Parameters:
    - email: The email address to validate.

    Raises:
    - ValueError: If the email format is invalid.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise ValueError("Invalid email format.")
```