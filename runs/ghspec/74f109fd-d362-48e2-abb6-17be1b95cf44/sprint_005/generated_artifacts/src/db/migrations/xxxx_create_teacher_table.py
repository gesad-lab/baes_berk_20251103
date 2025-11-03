```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.models.teacher import Teacher

class TeacherRepository:
    """Handles database interactions for Teacher entity."""

    def __init__(self, session: Session):
        self.session = session

    def create_teacher(self, name: str, email: str) -> Teacher:
        """Creates a new Teacher record in the database.

        Args:
            name (str): The name of the teacher.
            email (str): The email of the teacher.

        Returns:
            Teacher: The created Teacher instance.

        Raises:
            ValueError: If name or email is invalid or missing.
            IntegrityError: If the email already exists in the database.
        """
        if not name or not email:
            raise ValueError("Both name and email are required for teacher creation.")

        # Validate email format
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValueError("Invalid email format provided.")

        new_teacher = Teacher(name=name, email=email)
        try:
            self.session.add(new_teacher)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise IntegrityError("Email already exists, please use a different email.")
        
        return new_teacher

    def get_teacher_by_id(self, teacher_id: int) -> Teacher:
        """Retrieves a Teacher by their ID.

        Args:
            teacher_id (int): The ID of the teacher to retrieve.

        Returns:
            Teacher: The Teacher instance if found.

        Raises:
            ValueError: If the teacher does not exist.
        """
        teacher = self.session.query(Teacher).filter(Teacher.id == teacher_id).first()
        if teacher is None:
            raise ValueError(f"Teacher with ID {teacher_id} not found.")
        
        return teacher
```