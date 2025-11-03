```python
# src/services/teacher_service.py

from app.models import Teacher  # Importing the Teacher model for database interactions
from app import db  # Importing the database instance for CRUD operations
from sqlalchemy.exc import IntegrityError
from flask import abort

class TeacherService:
    """Service class for managing teacher information."""

    @staticmethod
    def create_teacher(name: str, email: str) -> Teacher:
        """
        Create a new teacher record.
        
        Args:
            name (str): The name of the teacher.
            email (str): The email of the teacher (must be unique).
        
        Returns:
            Teacher: The created Teacher instance.
        
        Raises:
            ValueError: If name or email is invalid.
            IntegrityError: If the email already exists in the database.
        """
        if not name or not email:
            raise ValueError("Both name and email are required.")

        new_teacher = Teacher(name=name, email=email)
        
        try:
            db.session.add(new_teacher)
            db.session.commit()
            return new_teacher
        except IntegrityError:
            db.session.rollback()  # Roll back the session in case of error
            abort(400, description="Email must be unique.")

    @staticmethod
    def get_all_teachers() -> list:
        """
        Retrieve a list of all teachers.
        
        Returns:
            List[Teacher]: A list of Teacher instances.
        """
        return Teacher.query.all()

    @staticmethod
    def update_teacher(teacher_id: int, name: str = None, email: str = None) -> Teacher:
        """
        Update an existing teacher's information.
        
        Args:
            teacher_id (int): The ID of the teacher to update.
            name (str, optional): The new name for the teacher.
            email (str, optional): The new email for the teacher.

        Returns:
            Teacher: The updated Teacher instance.
        
        Raises:
            ValueError: If the teacher_id is not found or invalid input is provided.
            IntegrityError: If the new email already exists in the database.
        """
        teacher = Teacher.query.get(teacher_id)
        if not teacher:
            abort(404, description="Teacher not found.")

        if email:
            teacher_with_email = Teacher.query.filter_by(email=email).first()
            if teacher_with_email and teacher_with_email.id != teacher_id:
                abort(400, description="Email must be unique.")
            teacher.email = email
        
        if name:
            teacher.name = name

        try:
            db.session.commit()
            return teacher
        except IntegrityError:
            db.session.rollback()
            abort(400, description="Email must be unique.")
```
