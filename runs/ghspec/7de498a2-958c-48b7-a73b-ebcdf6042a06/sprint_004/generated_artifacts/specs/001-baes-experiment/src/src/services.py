```python
# src/services.py

from sqlalchemy.orm import Session
from src.models import Student, Course  # Assuming these models exist
from sqlalchemy.exc import NoResultFound

def get_student_courses(db: Session, student_id: int):
    """
    Retrieve the list of courses for a specific student.

    Args:
        db (Session): The database session.
        student_id (int): The ID of the student to retrieve courses for.

    Returns:
        list: A list of courses the student is enrolled in.

    Raises:
        ValueError: If the student does not exist.
    """
    # Fetch the student from the database
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise ValueError(f"Student with ID {student_id} does not exist.")

    return student.courses  # Assuming `courses` is a relationship on the Student model
```