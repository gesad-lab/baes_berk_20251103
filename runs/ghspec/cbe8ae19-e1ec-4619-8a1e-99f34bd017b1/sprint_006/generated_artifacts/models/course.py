```python
# models/course.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New foreign key for Teacher

    # Relationship to the Teacher model
    teacher = relationship("Teacher", back_populates="courses")  # Establishing a back-reference

    def __init__(self, name, level, teacher_id=None):
        """Initializes a new Course instance."""
        self.name = name
        self.level = level
        self.teacher_id = teacher_id

    def __repr__(self):
        """String representation of the Course instance."""
        return f"<Course(id={self.id}, name={self.name}, level={self.level}, teacher_id={self.teacher_id})>"
```
