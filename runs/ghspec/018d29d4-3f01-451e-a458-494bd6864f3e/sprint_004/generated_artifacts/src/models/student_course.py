```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class StudentCourse(Base):
    """Represents the join table for the many-to-many relationship between Student and Course."""

    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Establish relationships with Student and Course models
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```