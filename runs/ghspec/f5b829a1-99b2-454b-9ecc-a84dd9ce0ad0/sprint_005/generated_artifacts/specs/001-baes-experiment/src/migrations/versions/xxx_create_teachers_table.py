```python
# File: src/services/teacher_service.py

from sqlalchemy.orm import Session
from src.models import Teacher  # Import the Teacher model for database interaction
from fastapi import HTTPException
import re

class TeacherService:
    """Service class for handling teacher-related operations."""

    def create_teacher(self, db: Session, name: str, email: str):
        """Create a new teacher in the database.

        Args:
            db (Session): Database session for performing operations.
            name (str): Name of the teacher (required).
            email (str): Email of the teacher (required).

        Raises:
            HTTPException: If name or email is missing, or email format is invalid.

        Returns:
            Teacher: The created Teacher object from the database.
        """
        # Check for missing fields
        if not name:
            raise HTTPException(status_code=400, detail="Name is required.")  # Error for missing name
        if not email:
            raise HTTPException(status_code=400, detail="Email is required.")  # Error for missing email
        
        # Validate email format using a regular expression
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise HTTPException(status_code=400, detail="Invalid email format.")  # Email format error

        # Create a new Teacher instance
        new_teacher = Teacher(name=name, email=email)
        db.add(new_teacher)  # Add the new teacher to the session
        db.commit()  # Commit the changes to the database
        db.refresh(new_teacher)  # Refresh the instance to get the newly assigned ID

        return new_teacher  # Return the created Teacher object to the caller
```