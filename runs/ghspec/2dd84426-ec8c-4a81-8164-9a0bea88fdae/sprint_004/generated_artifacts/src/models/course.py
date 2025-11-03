```python
# src/models/course.py

from sqlalchemy.orm import relationship
from .base import Base  # Assuming there's a base model defined somewhere

class Course(Base):
    __tablename__ = 'courses'
    # Existing attributes...
    
    # Establishing the relationship back-reference for students
    students = relationship("StudentCourses", back_populates="course")

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```