```python
# src/models/course.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # Add new field for teacher_id
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Allow nulls for courses without a teacher

    # Define relationship to Teacher
    teacher = relationship("Teacher", back_populates="courses")

    def __init__(self, name: str, teacher_id: int = None):
        """
        Initialize a Course instance.

        :param name: The name of the course.
        :param teacher_id: The ID of the teacher associated with the course (optional).
        """
        self.name = name
        self.teacher_id = teacher_id

    def assign_teacher(self, teacher_id: int):
        """
        Assign a teacher to the course.

        :param teacher_id: The ID of the teacher to assign.
        """
        self.teacher_id = teacher_id

    def remove_teacher(self):
        """
        Remove the teacher from the course.
        """
        self.teacher_id = None
```