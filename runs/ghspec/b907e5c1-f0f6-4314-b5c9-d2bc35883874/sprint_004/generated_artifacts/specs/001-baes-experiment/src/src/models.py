```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from your_application.models import Base  # Import the existing Base model

class StudentCourse(Base):
    """A model representing the many-to-many relationship between students and courses."""

    __tablename__ = 'student_courses'

    # Foreign keys for the relationships
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Relationships to the Student and Course models
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

    def __repr__(self):
        """Return a string representation of the StudentCourse."""
        return f"<StudentCourse(student_id={self.student_id}, course_id={self.course_id})>"
```