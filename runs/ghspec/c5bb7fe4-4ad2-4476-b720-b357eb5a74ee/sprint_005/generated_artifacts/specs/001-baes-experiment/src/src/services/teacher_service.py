```python
# src/services/teacher_service.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from src.models.teacher import Teacher  # Import the Teacher model
from typing import List, Optional

db = SQLAlchemy()

class TeacherService:
    """Service to handle business logic for Teacher entity."""

    @staticmethod
    def create_teacher(name: str, email: str) -> Teacher:
        """Create a new Teacher record in the database.

        Args:
            name (str): The name of the teacher.
            email (str): The email of the teacher.

        Returns:
            Teacher: The created Teacher instance.

        Raises:
            ValueError: If the email format is invalid or if the Teacher exists.
        """
        teacher = Teacher(name=name, email=email)
        
        try:
            db.session.add(teacher)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError(f"Teacher with email '{email}' already exists.")
        
        return teacher

    @staticmethod
    def get_teacher(teacher_id: int) -> Optional[Teacher]:
        """Retrieve a Teacher record by its ID.

        Args:
            teacher_id (int): The ID of the teacher.

        Returns:
            Optional[Teacher]: The Teacher instance if found, otherwise None.
        """
        return Teacher.query.get(teacher_id)

    @staticmethod
    def update_teacher(teacher_id: int, name: Optional[str] = None, email: Optional[str] = None) -> Teacher:
        """Update an existing Teacher record.

        Args:
            teacher_id (int): The ID of the teacher to update.
            name (Optional[str]): The new name of the teacher.
            email (Optional[str]): The new email of the teacher.

        Returns:
            Teacher: The updated Teacher instance.

        Raises:
            ValueError: If the Teacher with ID does not exist or if the new email format is invalid.
        """
        teacher = TeacherService.get_teacher(teacher_id)
        if not teacher:
            raise ValueError(f"Teacher with ID '{teacher_id}' does not exist.")
        
        if name:
            teacher.name = name
        if email:
            teacher.email = email
        
        db.session.commit()
        return teacher

    @staticmethod
    def list_teachers() -> List[Teacher]:
        """List all teachers in the database.

        Returns:
            List[Teacher]: A list of all Teacher instances.
        """
        return Teacher.query.all()
```