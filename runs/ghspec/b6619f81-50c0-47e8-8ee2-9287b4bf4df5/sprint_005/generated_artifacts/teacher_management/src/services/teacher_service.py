```python
# teacher_service.py

from typing import Optional, List
from sqlalchemy.exc import IntegrityError
from models import Teacher
from repositories.teacher_repository import TeacherRepository

class TeacherService:
    """Service class for managing Teacher records."""

    def __init__(self, repository: TeacherRepository):
        self.repository = repository

    def create_teacher(self, name: str, email: str) -> Teacher:
        """Create a new teacher record.

        Args:
            name (str): The name of the teacher.
            email (str): The email of the teacher.

        Returns:
            Teacher: The created Teacher object.

        Raises:
            ValueError: If either name or email is missing.
            IntegrityError: If the email already exists in the database.
        """
        if not name or not email:
            raise ValueError('Name and email must be provided.')

        new_teacher = Teacher(name=name, email=email)
        try:
            return self.repository.add(new_teacher)
        except IntegrityError:
            raise ValueError('Email already exists. Please use a different email.')

    def get_teacher(self, teacher_id: int) -> Optional[Teacher]:
        """Retrieve a teacher record by ID.

        Args:
            teacher_id (int): The ID of the teacher to retrieve.

        Returns:
            Optional[Teacher]: The Teacher object if found, otherwise None.
        """
        return self.repository.find_by_id(teacher_id)

    def update_teacher(self, teacher_id: int, name: Optional[str] = None, email: Optional[str] = None) -> Teacher:
        """Update an existing teacher's details.

        Args:
            teacher_id (int): The ID of the teacher to update.
            name (str, optional): The new name of the teacher. Defaults to None.
            email (str, optional): The new email of the teacher. Defaults to None.

        Returns:
            Teacher: The updated Teacher object.

        Raises:
            ValueError: If no new name or email is provided for the update.
            IntegrityError: If the email already exists in the database.
            LookupError: If the teacher is not found.
        """
        existing_teacher = self.get_teacher(teacher_id)
        if not existing_teacher:
            raise LookupError(f'Teacher with ID {teacher_id} not found.')

        if name:
            existing_teacher.name = name
        if email:
            existing_teacher.email = email

        try:
            return self.repository.update(existing_teacher)
        except IntegrityError:
            raise ValueError('Email already exists. Please use a different email.')
```