```python
# src/dal/teacher_dal.py

from typing import List, Optional
from sqlalchemy.orm import Session
from src.models.teacher import TeacherModel  # Import the Teacher model


class TeacherDAL:
    """Data Access Layer for Teacher entity, responsible for CRUD operations."""

    def __init__(self, db: Session):
        self.db = db

    def create_teacher(self, name: str, email: str) -> TeacherModel:
        """Create a new Teacher record in the database.

        Args:
            name (str): The name of the teacher.
            email (str): The email address of the teacher.

        Returns:
            TeacherModel: The created Teacher instance.
        """
        if not name or not email:
            raise ValueError("Both name and email are required")  # Input validation

        new_teacher = TeacherModel(name=name, email=email)
        self.db.add(new_teacher)
        self.db.commit()
        self.db.refresh(new_teacher)
        return new_teacher

    def get_teacher(self, teacher_id: int) -> Optional[TeacherModel]:
        """Retrieve a Teacher record by its ID.

        Args:
            teacher_id (int): The ID of the teacher to retrieve.

        Returns:
            Optional[TeacherModel]: The Teacher instance if found, None otherwise.
        """
        return self.db.query(TeacherModel).filter(TeacherModel.id == teacher_id).first()

    def get_all_teachers(self) -> List[TeacherModel]:
        """Retrieve all Teacher records.

        Returns:
            List[TeacherModel]: A list of all Teacher instances in the database.
        """
        return self.db.query(TeacherModel).all()
```