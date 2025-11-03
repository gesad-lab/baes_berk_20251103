```python
from app import db
from app.models import Teacher  # Import the Teacher model
from sqlalchemy.exc import IntegrityError
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TeacherDAL:
    """Data Access Layer for handling CRUD operations on Teacher entities."""

    @staticmethod
    def create_teacher(name: str, email: str) -> Teacher:
        """Creates and saves a new Teacher entity to the database.

        Args:
            name (str): The name of the teacher.
            email (str): The email of the teacher, must be unique.

        Returns:
            Teacher: The created Teacher object.

        Raises:
            ValueError: If the name or email is missing.
            IntegrityError: If the email is already in use.
        """
        if not name or not email:
            raise ValueError("Both name and email are required.")

        teacher = Teacher(name=name, email=email)
        db.session.add(teacher)
        try:
            db.session.commit()
            logger.info("Teacher created successfully: %s", teacher)
            return teacher
        except IntegrityError:
            db.session.rollback()
            logger.error("Failed to create teacher with email %s: Email must be unique.", email)
            raise

    @staticmethod
    def get_all_teachers() -> list:
        """Retrieves all Teacher entities from the database.

        Returns:
            list: A list of all Teacher objects.
        """
        teachers = Teacher.query.all()
        logger.info("Retrieved all teachers, count: %d", len(teachers))
        return teachers

    @staticmethod
    def update_teacher(teacher_id: int, name: str, email: str) -> Teacher:
        """Updates an existing Teacher entity in the database.

        Args:
            teacher_id (int): The ID of the teacher to update.
            name (str): The new name for the teacher.
            email (str): The new email for the teacher.

        Returns:
            Teacher: The updated Teacher object.

        Raises:
            ValueError: If the teacher_id is not found or the provided name or email is missing.
        """
        teacher = Teacher.query.get(teacher_id)
        if not teacher:
            raise ValueError(f"Teacher with ID {teacher_id} does not exist.")
        if not name or not email:
            raise ValueError("Both name and email are required.")

        teacher.name = name
        teacher.email = email
        db.session.commit()
        logger.info("Teacher updated successfully: %s", teacher)
        return teacher
```