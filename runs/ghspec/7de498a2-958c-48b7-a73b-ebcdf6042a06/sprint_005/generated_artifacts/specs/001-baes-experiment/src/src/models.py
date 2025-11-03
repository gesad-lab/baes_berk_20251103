```python
from sqlalchemy.orm import Session
from src.models import Teacher

def create_teacher(db: Session, name: str, email: str):
    """Create a new Teacher in the database.

    Args:
        db (Session): The database session.
        name (str): The name of the teacher.
        email (str): The email address of the teacher.

    Returns:
        Teacher: The created Teacher object.
    """
    # Validate input (basic validation)
    if not name or not email:
        raise ValueError("Name and email are required.")

    new_teacher = Teacher(name=name, email=email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

def get_teacher(db: Session, teacher_id: int):
    """Retrieve a Teacher by their ID.

    Args:
        db (Session): The database session.
        teacher_id (int): The ID of the teacher to retrieve.

    Returns:
        Teacher: The Teacher object if found, otherwise None.
    """
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()

def update_teacher(db: Session, teacher_id: int, name: str = None, email: str = None):
    """Update the details of an existing Teacher.

    Args:
        db (Session): The database session.
        teacher_id (int): The ID of the teacher to update.
        name (str, optional): New name for the teacher.
        email (str, optional): New email for the teacher.

    Returns:
        Teacher: The updated Teacher object if successful, otherwise None.
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher:
        if name:
            teacher.name = name
        if email:
            teacher.email = email
        db.commit()
        return teacher
    return None

def delete_teacher(db: Session, teacher_id: int):
    """Delete a Teacher from the database.

    Args:
        db (Session): The database session.
        teacher_id (int): The ID of the teacher to delete.

    Returns:
        bool: True if deletion was successful, False otherwise.
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher:
        db.delete(teacher)
        db.commit()
        return True
    return False
```