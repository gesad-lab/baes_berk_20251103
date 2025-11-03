```python
# File: src/services/teacher_service.py

from your_app import db  # Adjust the import to your app structure
from your_app.models import Teacher  # Import the Teacher model
from sqlalchemy.exc import IntegrityError, DataError

def create_teacher(name: str, email: str) -> dict:
    """Create a new teacher and return their details.

    Args:
        name (str): The name of the teacher.
        email (str): The email of the teacher.

    Returns:
        dict: A dictionary containing the created teacher's details.
    """
    # Validate input
    if not name or not email:
        raise ValueError("Both name and email are required.")

    # Create a new Teacher instance
    new_teacher = Teacher(name=name, email=email)

    try:
        # Add the new teacher to the session and commit
        db.session.add(new_teacher)
        db.session.commit()
    except (IntegrityError, DataError) as e:
        db.session.rollback()  # Rollback in case of error
        raise ValueError(f"Error creating teacher: {str(e)}")

    return {
        "id": new_teacher.id,
        "name": new_teacher.name,
        "email": new_teacher.email
    }

def get_teacher_by_id(teacher_id: int) -> dict:
    """Fetch details of a teacher based on their ID.

    Args:
        teacher_id (int): The unique identifier of the teacher.

    Returns:
        dict: A dictionary containing the teacher's details, or None if not found.
    """
    # Fetch the teacher by ID
    teacher = Teacher.query.get(teacher_id)

    if teacher is None:
        raise ValueError("Teacher not found.")

    return {
        "id": teacher.id,
        "name": teacher.name,
        "email": teacher.email
    }
```