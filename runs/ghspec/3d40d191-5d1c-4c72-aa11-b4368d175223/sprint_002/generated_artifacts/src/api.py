```python
# src/services.py

from sqlalchemy.orm import Session
from src.models import Student

def create_student(session: Session, name: str, email: str):
    """
    Create a new Student in the database with the given name and email.

    Parameters:
    - session: Database session to execute the operation.
    - name (str): Name of the student.
    - email (str): Email of the student.

    Returns:
    - Student: The created Student object.

    Raises:
    - ValueError: If name or email is not provided.
    """
    if not name or not email:
        raise ValueError("Both name and email are required to create a student.")

    student = Student(name=name, email=email)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

def get_students(session: Session):
    """
    Retrieve all Student records from the database.

    Parameters:
    - session: Database session to execute the operation.

    Returns:
    - List[Student]: A list of all Student objects.
    """
    return session.query(Student).all()
```