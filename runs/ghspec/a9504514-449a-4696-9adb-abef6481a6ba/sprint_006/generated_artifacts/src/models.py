```python
# src/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Teacher(Base):
    """Represents a teacher in the system."""
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    # Relationship back to courses
    courses = relationship("Course", back_populates="teacher")

class Course(Base):
    """Represents a course in the system."""
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Optional teacher assignment

    # Establish the relationship with the Teacher
    teacher = relationship("Teacher", back_populates="courses")

    def assign_teacher(self, teacher):
        """Assign a teacher to this course."""
        if not isinstance(teacher, Teacher):
            raise ValueError("Invalid teacher assignment.")
        self.teacher = teacher
```

