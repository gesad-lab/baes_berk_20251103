```python
# src/services.py

from typing import List
from sqlalchemy.orm import Session
from src.models import Student
from src.database import get_student_by_email, get_students as fetch_students

def create_student(session: Session, name: str, email: str) -> Student:
    """
    Creates a new student in the database.

    Args:
        session (Session): Database session to use for the operation.
        name (str): The name of the student.
        email (str): The email of the student.

    Returns:
        Student: The created Student object.
    """
    # Validate email format
    if not email or '@' not in email:
        raise ValueError("Invalid email format")

    new_student = Student(name=name, email=email)
    session.add(new_student)
    session.commit()
    session.refresh(new_student)
    return new_student

def get_students(session: Session) -> List[Student]:
    """
    Retrieves all students from the database.

    Args:
        session (Session): Database session to use for the operation.

    Returns:
        List[Student]: List of Student objects from the database.
    """
    return fetch_students(session=session)

# Ensure to handle database rollbacks on errors to maintain integrity
```