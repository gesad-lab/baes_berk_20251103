```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base  # Assuming a base class is being imported from a base module

class StudentCourse(Base):
    """Model to define the many-to-many relationship between Students and Courses."""

    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Relationships
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

    def __repr__(self):
        """Return a string representation of the StudentCourse entry."""
        return f"<StudentCourse(student_id={self.student_id}, course_id={self.course_id})>"
```