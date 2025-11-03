```python
# src/models/student.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base  # Assuming Base is your declarative base for models
from src.models.student_courses import StudentCourses  # Import junction table

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Establishing relationship to the StudentCourses junction table
    courses = relationship('StudentCourses', back_populates='student')

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"

    def enroll_in_course(self, course_id):
        """Enroll the student in a course by course_id."""
        # Append new StudentCourses entry for the student
        new_enrollment = StudentCourses(student_id=self.id, course_id=course_id)
        return new_enrollment

    def unenroll_from_course(self, course_id):
        """Remove the enrollment of the course from the student."""
        # Logic to remove the specific enrollment based on course_id (to be implemented)
        pass
```