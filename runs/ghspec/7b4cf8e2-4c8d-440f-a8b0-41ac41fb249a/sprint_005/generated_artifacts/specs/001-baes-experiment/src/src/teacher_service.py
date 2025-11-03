```python
from models import Teacher
from app import db
from sqlalchemy.exc import IntegrityError

def create_teacher(name: str, email: str) -> Teacher:
    """Creates a new teacher record with the given name and email.

    Args:
        name (str): The name of the teacher.
        email (str): The email of the teacher.

    Returns:
        Teacher: The created Teacher object.

    Raises:
        ValueError: If the email is already in use.
    """
    new_teacher = Teacher(name=name, email=email)
    db.session.add(new_teacher)
    try:
        db.session.commit()
        return new_teacher
    except IntegrityError:
        db.session.rollback()
        raise ValueError(f"E001: Email '{email}' is already in use.")

def get_teacher(teacher_id: int) -> Teacher:
    """Retrieves a teacher by their ID.

    Args:
        teacher_id (int): The ID of the teacher.

    Returns:
        Teacher: The Teacher object corresponding to the given ID.

    Raises:
        ValueError: If the teacher is not found.
    """
    teacher = Teacher.query.get(teacher_id)
    if teacher is None:
        raise ValueError(f"E002: Teacher with ID '{teacher_id}' not found.")
    return teacher

def list_teachers() -> list:
    """Retrieves all teachers in the system.

    Returns:
        list: A list of Teacher objects.
    """
    return Teacher.query.all()
```