```python
# src/services/teacher_service.py

from typing import Dict, Any
from src.models.teacher import Teacher
from src.repositories.teacher_repository import TeacherRepository

class TeacherService:
    """Service for managing teachers in the system, including creation and retrieval of teacher data."""

    def __init__(self, repository: TeacherRepository):
        self.repository = repository

    def create_teacher(self, name: str, email: str) -> Dict[str, Any]:
        """Creates a new teacher with the provided name and email.
        
        Args:
            name (str): The name of the teacher.
            email (str): The email of the teacher.

        Returns:
            dict: A confirmation dictionary with the teacher ID and details.

        Raises:
            ValueError: If required fields are missing or invalid.
        """
        # Input validation
        if not name:
            raise ValueError("Name is required")
        if not email:
            raise ValueError("Email is required")
        
        # Create a new Teacher entry
        teacher = Teacher(name=name, email=email)
        
        # Persist to the repository
        teacher_id = self.repository.add(teacher)

        return {
            "id": teacher_id,
            "name": teacher.name,
            "email": teacher.email
        }

    def get_teacher(self, teacher_id: str) -> Dict[str, Any]:
        """Retrieves a teacher by ID.

        Args:
            teacher_id (str): The ID of the teacher to retrieve.

        Returns:
            dict: A dictionary containing the teacher's details.

        Raises:
            ValueError: If the teacher was not found.
        """
        # Retrieve the teacher from the repository
        teacher = self.repository.get_by_id(teacher_id)
        
        if not teacher:
            raise ValueError("Teacher not found")

        return {
            "id": teacher.id,
            "name": teacher.name,
            "email": teacher.email
        }
```
