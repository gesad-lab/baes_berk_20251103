```python
# src/services/teacher_service.py

from src.models.teacher import Teacher
from src.repositories.teacher_repository import (
    create_teacher,
    get_teacher_by_id,
)
from fastapi import HTTPException, status

class TeacherService:
    """
    Service layer for managing Teacher entities.
    """

    @staticmethod
    def create_teacher(name: str, email: str) -> Teacher:
        """
        Creates a new Teacher entity.

        :param name: The name of the Teacher (required).
        :param email: The email of the Teacher (required, unique).
        :return: The created Teacher entity.
        :raises HTTPException: If validation fails or email is not unique.
        """
        if not name or not email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Name and email must be provided.",
            )
        
        # Check if email already exists
        existing_teacher = get_teacher_by_id(email=email)
        if existing_teacher:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email must be unique.",
            )

        # Create the new teacher
        new_teacher = create_teacher(name=name, email=email)
        return new_teacher

    @staticmethod
    def get_teacher(teacher_id: int) -> Teacher:
        """
        Retrieves the Teacher entity by its ID.

        :param teacher_id: The unique ID of the Teacher.
        :return: The Teacher entity.
        :raises HTTPException: If the teacher is not found.
        """
        teacher = get_teacher_by_id(teacher_id)
        if not teacher:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found.",
            )
        return teacher
```