```python
from sqlalchemy.orm import Session
from models import Teacher
from sqlalchemy.exc import IntegrityError
from typing import List, Dict, Any

def create_teacher(name: str, email: str, db: Session) -> Teacher:
    """Create a new Teacher record in the database.

    Args:
        name (str): The name of the teacher.
        email (str): The email of the teacher.
        db (Session): The database session.

    Returns:
        Teacher: The created Teacher object.

    Raises:
        ValueError: If the name or email is not provided.
        IntegrityError: If the email already exists in the database.
    """
    if not name or not email:
        raise ValueError("Both name and email are required.")

    new_teacher = Teacher(name=name, email=email)
    db.add(new_teacher)
    
    try:
        db.commit()
        db.refresh(new_teacher)
    except IntegrityError:
        db.rollback()
        raise ValueError(f"Email '{email}' is already in use.")

    return new_teacher

def get_teachers(db: Session) -> List[Dict[str, Any]]:
    """Retrieve the list of existing teachers from the database.

    Args:
        db (Session): The database session.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing teacher details.
    """
    teachers = db.query(Teacher).all()
    return [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]
```