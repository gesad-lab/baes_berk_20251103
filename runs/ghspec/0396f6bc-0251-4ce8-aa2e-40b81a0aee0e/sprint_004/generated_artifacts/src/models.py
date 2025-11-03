```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import Base, Student, Course

class StudentCourses(Base):
    """Mapping table for many-to-many relationship between Students and Courses."""
    
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    
    # Define relationships for ORM
    student = relationship('Student', back_populates='courses')
    course = relationship('Course', back_populates='students')

# Establishing relationships in the Student and Course models
Student.courses = relationship('StudentCourses', back_populates='student')
Course.students = relationship('StudentCourses', back_populates='course')
```