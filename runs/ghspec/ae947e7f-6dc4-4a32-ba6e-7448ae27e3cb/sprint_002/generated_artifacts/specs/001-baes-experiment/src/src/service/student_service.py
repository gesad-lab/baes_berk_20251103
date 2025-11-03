```python
# src/service/student_service.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.model.student import Student
from pydantic import EmailStr, ValidationError


def create_student(session: Session, name: str, email: str) -> Student:
    """
    Create a new student in the database.

    Args:
        session (Session): SQLAlchemy session to interact with the database.
        name (str): The name of the student.
        email (str): The email of the student.

    Returns:
        Student: The created student object.

    Raises:
        ValueError: If the email format is invalid or if the student creation fails due to duplicate email.
    """
    # Validate the email format
    try:
        email_validated = EmailStr.validate(email)
    except ValidationError:
        raise ValueError("Invalid email format.")

    # Create a new Student instance
    new_student = Student(name=name, email=email_validated)

    try:
        session.add(new_student)
        session.commit()
        session.refresh(new_student)  # Refresh instance to get assigned ID
        return new_student
    except IntegrityError:
        session.rollback()  # Rollback the session on error
        raise ValueError("Email already exists. Please use a different email.")

def get_student_by_id(session: Session, student_id: int) -> Student:
    """
    Retrieve a student by their ID.

    Args:
        session (Session): SQLAlchemy session to interact with the database.
        student_id (int): The ID of the student to retrieve.

    Returns:
        Student: The student object if found.

    Raises:
        ValueError: If no student with the given ID is found.
    """
    student = session.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise ValueError("Student not found.")
    return student
```