```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class StudentCourse(Base):
    """Model for the relationship between students and courses."""
    
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Define relationships for easy access
    student = relationship('Student', back_populates='courses')
    course = relationship('Course', back_populates='students')

# Ensure that the Student and Course models have appropriate relationships defined
from models import Student, Course

# Adding a relationship field in the Student model (assuming already defined in the project)
Student.courses = relationship('StudentCourse', back_populates='student', cascade="all, delete-orphan")
# Adding a relationship field in the Course model (assuming already defined in the project)
Course.students = relationship('StudentCourse', back_populates='course', cascade="all, delete-orphan")
```