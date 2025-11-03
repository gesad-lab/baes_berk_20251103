```python
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from .models import Teacher
from .schemas import TeacherCreate
import re
from uuid import uuid4

# Function to create a new Teacher record in the database
def create_teacher(db: Session, teacher: TeacherCreate) -> Teacher:
    # Validate email format
    if not is_valid_email(teacher.email):
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E001", "message": "Invalid email format", "details": {}}},
        )

    # Create a new Teacher instance
    db_teacher = Teacher(
        id=str(uuid4()),  # Generate a unique ID
        name=teacher.name,
        email=teacher.email,
    )

    # Try to add the new teacher to the session and commit
    try:
        db.add(db_teacher)
        db.commit()
        db.refresh(db_teacher)  # Refresh to get the created instance with ID
        return db_teacher
    except IntegrityError:
        # Handle cases where email already exists
        db.rollback()  # Rollback the session
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E002", "message": "Email already exists", "details": {}}},
        )


# Helper function to validate email format
def is_valid_email(email: str) -> bool:
    # Simple regex for basic email validation
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None
```