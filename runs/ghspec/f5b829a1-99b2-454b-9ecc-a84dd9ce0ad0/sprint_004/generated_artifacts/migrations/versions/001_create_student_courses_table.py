```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Enrollment(Base):
    """Model for the Enrollment bridge table that links students and courses."""
    
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    
    # Relationships
    student = relationship('Student', back_populates='courses')
    course = relationship('Course', back_populates='students')

# Add relationship fields to the Student and Course models
from src.models.student import Student
from src.models.course import Course

# Inside Student model
Student.courses = relationship(
    'Enrollment',
    back_populates='student',
    cascade='all, delete',
    passive_deletes=True
)

# Inside Course model
Course.students = relationship(
    'Enrollment',
    back_populates='course',
    cascade='all, delete',
    passive_deletes=True
)
```