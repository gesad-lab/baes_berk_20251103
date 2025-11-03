```python
# File: validators/course_validator.py

from fastapi import HTTPException
from models.teacher import Teacher  # Importing the Teacher model
from db.database import Session  # Importing the session for database access

class CourseValidator:
    @staticmethod
    def validate_teacher_id(teacher_id: str):
        """
        Validate the provided teacher ID to ensure the teacher exists.

        Parameters:
        - teacher_id (str): The ID of the teacher to validate.

        Raises:
        - HTTPException: If validation fails, returns 404 with a specific message.
        """
        if not teacher_id:
            raise HTTPException(status_code=400, detail="Teacher ID is required.")

        # Create a database session to interact with the database
        with Session() as session:
            teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
            if teacher is None:
                raise HTTPException(status_code=404, detail="Teacher not found.")
```