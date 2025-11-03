from repositories.teacher_repository import TeacherRepository
from sqlalchemy.exc import NoResultFound

class TeacherService:
    """Encapsulates business logic for Teacher operations."""

    def __init__(self):
        self.teacher_repo = TeacherRepository()

    def create_teacher(self, name, email):
        if not name or not email:
            raise ValueError("Both name and email fields are required.")
        if not self.validate_email(email):
            raise ValueError("Email format is invalid.")

        return self.teacher_repo.create_teacher(name, email)

    def validate_email(self, email):
        import re
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def get_teacher(self, teacher_id):
        """
        Retrieve a teacher by their unique ID.

        Args:
            teacher_id (int): The ID of the teacher to retrieve.

        Returns:
            Teacher: The Teacher object if found.

        Raises:
            ValueError: If the teacher_id is invalid.
            NoResultFound: If no teacher is found with the given ID.
        """
        if not isinstance(teacher_id, int) or teacher_id <= 0:
            raise ValueError("Invalid teacher ID. It must be a positive integer.")

        teacher = self.teacher_repo.get_teacher(teacher_id)
        if not teacher:
            raise NoResultFound(f"No teacher found with ID: {teacher_id}")
        return teacher