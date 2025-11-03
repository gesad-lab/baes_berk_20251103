```python
# File: src/models/course.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base
from typing import Optional

class Course(Base):
    """
    Course model representing a course in the system.

    Attributes:
    - id: Unique identifier for the course.
    - name: Name of the course.
    - teacher_id: Optional foreign key reference to the associated Teacher.
    """
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New foreign key relationship

    # Establish relationship with Teacher model
    teacher = relationship("Teacher", back_populates="courses")

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, teacher_id={self.teacher_id})>"
```

