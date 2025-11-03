```python
# src/data_access/teacher_dal.py

from typing import Optional, List
from sqlalchemy.orm import Session
from src.models import Teacher  # Assuming Teacher model is in src/models.py
from sqlalchemy.exc import IntegrityError

class TeacherDAL:
    """Data Access Layer for Teacher entity to handle CRUD operations."""

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_teacher(self, name: str, email: str) -> Teacher:
        """Create a new teacher in the database."""
        if not name or not email:
            raise ValueError("Both name and email are required.")
        
        new_teacher = Teacher(name=name, email=email)
        self.db_session.add(new_teacher)
        try:
            self.db_session.commit()
        except IntegrityError:
            self.db_session.rollback()
            raise ValueError("Email must be unique.")
        
        return new_teacher

    def get_teacher(self, teacher_id: int) -> Optional[Teacher]:
        """Retrieve a teacher by their ID."""
        return self.db_session.query(Teacher).filter_by(id=teacher_id).first()

    def update_teacher(self, teacher_id: int, name: Optional[str] = None, email: Optional[str] = None) -> Optional[Teacher]:
        """Update a teacher's information."""
        teacher = self.get_teacher(teacher_id)
        if teacher is None:
            return None

        if name:
            teacher.name = name
        if email:
            teacher.email = email
        
        self.db_session.commit()
        return teacher

    def delete_teacher(self, teacher_id: int) -> bool:
        """Delete a teacher from the database."""
        teacher = self.get_teacher(teacher_id)
        if teacher is None:
            return False
        
        self.db_session.delete(teacher)
        self.db_session.commit()
        return True

    def get_all_teachers(self) -> List[Teacher]:
        """Retrieve a list of all teachers."""
        return self.db_session.query(Teacher).all()
```