```python
# src/repositories/teacher_repository.py

from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from src.models.teacher import Teacher

class TeacherRepository:
    """Handles database operations related to the Teacher entity."""

    def __init__(self, db_session):
        self.db_session = db_session

    def create_teacher(self, name: str, email: str):
        """Create a new teacher in the database.

        Args:
            name (str): The name of the teacher.
            email (str): The email of the teacher.

        Raises:
            ValueError: If the name or email is invalid or missing.
            Exception: If an error occurs while saving to the database.

        Returns:
            Teacher: The created Teacher object.
        """
        self.validate_teacher_data(name, email)

        new_teacher = Teacher(name=name, email=email)

        try:
            self.db_session.add(new_teacher)
            self.db_session.commit()
        except IntegrityError as e:
            # Rollback in case of error and raise a user-friendly message
            self.db_session.rollback()
            raise Exception(f"Failed to create teacher: {str(e)}")
        except Exception as e:
            self.db_session.rollback()
            raise Exception(f"An error occurred while creating a teacher: {str(e)}")

        return new_teacher

    @staticmethod
    def validate_teacher_data(name: str, email: str):
        """Validate the required fields for teacher creation.

        Args:
            name (str): The name of the teacher.
            email (str): The email of the teacher.

        Raises:
            ValueError: If the name or email is invalid or missing.
        """
        if not name or not isinstance(name, str):
            raise ValueError('Name is required and must be a string.')
        
        if not email or not isinstance(email, str):
            raise ValueError('Email is required and must be a string.')
        
        # Additional validation can be added (e.g., email format)

```