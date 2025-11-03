```python
# src/services.py

from src.models import Teacher  # Import the Teacher model to interact with teacher records
from src.database import get_db_session  # Import the database session manager
from sqlalchemy.exc import IntegrityError  # Handle specific database exceptions
from typing import Optional, List

def create_teacher(name: str, email: str) -> Teacher:
    """
    Create a new teacher entity in the database.

    Parameters:
        name (str): The full name of the teacher.
        email (str): The email address of the teacher.

    Returns:
        Teacher: The created Teacher object with assigned attributes.

    Raises:
        ValueError: If the teacher name or email is invalid.
    """
    if not name or not email:
        raise ValueError("Teacher name and email must not be empty.")
    
    session = get_db_session()
    new_teacher = Teacher(name=name, email=email)

    try:
        session.add(new_teacher)
        session.commit()
    except IntegrityError:
        session.rollback()
        raise ValueError("A teacher with this email already exists.")
    finally:
        session.close()

    return new_teacher


def get_teacher_by_id(teacher_id: int) -> Optional[Teacher]:
    """
    Retrieve a teacher by their ID.

    Parameters:
        teacher_id (int): The ID of the teacher to retrieve.

    Returns:
        Optional[Teacher]: The Teacher object if found, otherwise None.
    """
    session = get_db_session()
    
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    session.close()
    
    return teacher


def get_all_teachers() -> List[Teacher]:
    """
    Retrieve all teachers from the database.

    Returns:
        List[Teacher]: A list of all Teacher objects.
    """
    session = get_db_session()

    teachers = session.query(Teacher).all()
    session.close()

    return teachers
```