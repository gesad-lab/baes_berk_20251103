```python
# File: src/models/student.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    """Represents a student in the educational system."""

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)

    # Establishing a many-to-many relationship with Course using the StudentCourses join table
    courses = relationship("StudentCourses", back_populates="student")

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"

# Ensure to import the necessary model for the join relationship
from .student_courses import StudentCourses
```