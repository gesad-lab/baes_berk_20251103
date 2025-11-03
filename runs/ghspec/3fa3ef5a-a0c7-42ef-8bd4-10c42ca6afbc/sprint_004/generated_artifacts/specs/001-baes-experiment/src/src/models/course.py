```python
# src/models/course.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.db import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(String)

    # Define a many-to-many relationship with students through the associated student_courses table
    students = relationship("Student", secondary="student_courses", back_populates="courses")

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"

    # Add any additional methods or properties to manage the course entity if required
```