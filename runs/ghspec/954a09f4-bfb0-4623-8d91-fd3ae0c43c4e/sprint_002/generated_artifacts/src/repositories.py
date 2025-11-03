```python
# src/repositories.py

from src.models import Student
from sqlalchemy.exc import IntegrityError

def create_student(name: str, email: str) -> Student:
    """Create a new student with the given name and email.

    Parameters:
        name (str): The name of the student.
        email (str): The email of the student.

    Returns:
        Student: The created student object.

    Raises:
        ValueError: If the email is not provided.
    """
    if not email:
        raise ValueError("The email is required to create a student.")

    # Create a new Student instance
    new_student = Student(name=name, email=email)

    try:
        db.session.add(new_student)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise ValueError("The email provided is already in use.")

    return new_student


def get_student(student_id: int) -> Student:
    """Retrieve a student by their ID.

    Parameters:
        student_id (int): The ID of the student.

    Returns:
        Student: The student with the specified ID.

    Raises:
        ValueError: If the student is not found.
    """
    student = Student.query.get(student_id)
    if not student:
        raise ValueError(f"Student with ID {student_id} not found.")
    return student
```