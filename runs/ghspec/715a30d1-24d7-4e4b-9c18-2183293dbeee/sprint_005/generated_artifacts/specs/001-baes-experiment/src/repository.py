```python
# repository.py

from sqlalchemy.orm import Session
from models import Teacher  # Assuming Teacher model is defined in models.py
from typing import List

class TeacherRepository:
    """Repository for managing Teacher entities."""

    def __init__(self, db: Session):
        self.db = db

    def create_teacher(self, name: str, email: str) -> Teacher:
        """Create a new teacher in the database.
        
        Args:
            name (str): The name of the teacher.
            email (str): The email of the teacher.

        Returns:
            Teacher: The created Teacher object.
        """
        new_teacher = Teacher(name=name, email=email)
        self.db.add(new_teacher)
        self.db.commit()
        self.db.refresh(new_teacher)
        return new_teacher

    def get_teacher_by_id(self, teacher_id: int) -> Teacher:
        """Retrieve a teacher by their ID.
        
        Args:
            teacher_id (int): The ID of the teacher to retrieve.

        Returns:
            Teacher: The teacher object.

        Raises:
            ValueError: If the teacher is not found.
        """
        teacher = self.db.query(Teacher).filter(Teacher.id == teacher_id).first()
        if teacher is None:
            raise ValueError(f"Teacher with ID {teacher_id} not found.")
        return teacher

    def get_all_teachers(self) -> List[Teacher]:
        """Retrieve all teachers from the database.
        
        Returns:
            List[Teacher]: A list of all Teacher objects.
        """
        return self.db.query(Teacher).all()

    def delete_teacher(self, teacher_id: int) -> bool:
        """Delete a teacher by their ID.
        
        Args:
            teacher_id (int): The ID of the teacher to delete.

        Returns:
            bool: True if the teacher was deleted, False otherwise.
        """
        teacher = self.get_teacher_by_id(teacher_id)
        if teacher:
            self.db.delete(teacher)
            self.db.commit()
            return True
        return False
```