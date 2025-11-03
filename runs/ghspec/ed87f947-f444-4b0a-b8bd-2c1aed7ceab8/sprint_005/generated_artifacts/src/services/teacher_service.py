```python
# src/services/teacher_service.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional

Base = declarative_base()

# Teacher model for database interaction
class Teacher(Base):
    """Model representing a teacher in the database."""
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

# Service class for managing teacher-related operations
class TeacherService:
    """Service for managing teacher entities."""
    
    def __init__(self, session_factory: sessionmaker):
        """Initialize the service with a SQLAlchemy session factory."""
        self.session_factory = session_factory

    def create_teacher(self, name: str, email: str) -> Teacher:
        """Create a new teacher record.

        :param name: The name of the teacher.
        :param email: The email address of the teacher.
        :return: The created Teacher object.
        :raises ValueError: If name or email is invalid.
        """
        if not name or not email:
            raise ValueError("Both name and email must be provided.")
        
        new_teacher = Teacher(name=name, email=email)
        
        with self.session_factory() as session:
            session.add(new_teacher)
            session.commit()
            session.refresh(new_teacher)  # Load the new data from the database

        return new_teacher

    def get_teacher(self, teacher_id: int) -> Optional[Teacher]:
        """Retrieve a teacher by ID.

        :param teacher_id: The ID of the teacher to retrieve.
        :return: The corresponding Teacher object, or None if not found.
        """
        with self.session_factory() as session:
            return session.query(Teacher).filter(Teacher.id == teacher_id).first()

    def update_teacher(self, teacher_id: int, name: Optional[str] = None, email: Optional[str] = None) -> Optional[Teacher]:
        """Update a teacher's information.

        :param teacher_id: The ID of the teacher to update.
        :param name: The new name of the teacher.
        :param email: The new email address of the teacher.
        :return: The updated Teacher object, or None if not found.
        :raises ValueError: If both name and email are None.
        """
        if name is None and email is None:
            raise ValueError("At least one of name or email must be provided.")

        with self.session_factory() as session:
            teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()  # Find the teacher by ID
            if not teacher:
                return None  # Teacher not found

            if name:
                teacher.name = name
            if email:
                teacher.email = email

            session.commit()
            session.refresh(teacher)  # Refresh the updated teacher object

        return teacher

    def delete_teacher(self, teacher_id: int) -> bool:
        """Delete a teacher by ID.

        :param teacher_id: The ID of the teacher to delete.
        :return: True if the teacher was deleted, False if not found.
        """
        with self.session_factory() as session:
            teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
            if not teacher:
                return False  # Teacher not found

            session.delete(teacher)
            session.commit()
        
        return True
```