```python
# src/services.py

from sqlalchemy.orm import Session
from models import Teacher
from fastapi import HTTPException

def create_teacher(name: str, email: str, db: Session) -> Teacher:
    """
    Create a new teacher with the provided name and email.

    Args:
        name (str): The name of the teacher.
        email (str): The email address of the teacher.
        db (Session): Database session.

    Returns:
        Teacher: The created Teacher object.

    Raises:
        HTTPException: If the input validation fails for name or email.
    """
    # Validate input fields
    if not name or not email:
        raise HTTPException(
            status_code=400,
            detail={
                "error": {
                    "code": "E001",
                    "message": "Name and email are required fields.",
                    "details": {
                        "missing": ["name"] if not name else [],
                        "missing": ["email"] if not email else []
                    }
                }
            }
        )
    
    # Check if email is valid (basic check)
    if "@" not in email:
        raise HTTPException(
            status_code=400,
            detail={
                "error": {
                    "code": "E002",
                    "message": "Invalid email format.",
                }
            }
        )
    
    # Create a new teacher instance
    new_teacher = Teacher(name=name, email=email)

    # Add the teacher to the session and commit to the database
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    
    return new_teacher

def retrieve_teachers(db: Session):
    """
    Retrieve all teachers from the database.

    Args:
        db (Session): Database session.

    Returns:
        List[Teacher]: A list of Teacher objects.
    """
    return db.query(Teacher).all()
```