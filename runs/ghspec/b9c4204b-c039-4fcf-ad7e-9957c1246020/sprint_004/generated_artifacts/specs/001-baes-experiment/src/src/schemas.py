```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base  # Import the Base from your database module

class StudentCourse(Base):
    """Model to represent the many-to-many relationship between students and courses."""
    __tablename__ = "student_courses"

    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Update the Student and Course models to include the relationship
from src.models import Student, Course  # Ensure you have these imports

Student.courses = relationship("StudentCourse", back_populates="student")
Course.students = relationship("StudentCourse", back_populates="course")
```