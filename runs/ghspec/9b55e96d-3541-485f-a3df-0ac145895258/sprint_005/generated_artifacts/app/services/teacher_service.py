```python
from sqlalchemy.orm import Session
from models import Teacher
from database import get_db

class TeacherService:
    """Service layer to handle business logic for Teacher entities."""

    @staticmethod
    def create_teacher(name: str, email: str, db: Session) -> dict:
        """Creates a new Teacher entity in the database.

        Args:
            name (str): The name of the teacher.
            email (str): The email of the teacher.
            db (Session): The database session.

        Returns:
            dict: A message confirming successful creation and the teacher's ID.

        Raises:
            ValueError: If name or email is empty.
            ConflictError: If an email already exists in the database.
        """
        if not name or not email:
            raise ValueError({"error": {"code": "E001", "message": "Name and email are required fields."}})
        
        # Check for existing teacher with the same email
        existing_teacher = db.query(Teacher).filter(Teacher.email == email).first()
        if existing_teacher:
            raise ValueError({"error": {"code": "E002", "message": "Email already exists."}})

        # Create new Teacher object and add to session
        teacher = Teacher(name=name, email=email)
        db.add(teacher)
        db.commit()

        return {"message": "Teacher created successfully", "teacher_id": teacher.id}

    @staticmethod
    def get_teacher(teacher_id: int, db: Session) -> dict:
        """Retrieves a Teacher entity by ID.

        Args:
            teacher_id (int): The ID of the teacher to retrieve.
            db (Session): The database session.

        Returns:
            dict: A dictionary containing the teacher's ID, name, and email.

        Raises:
            NotFoundError: If the teacher cannot be found.
        """
        teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
        if not teacher:
            raise ValueError({"error": {"code": "E003", "message": "Teacher not found."}})
        
        return {"id": teacher.id, "name": teacher.name, "email": teacher.email}
```