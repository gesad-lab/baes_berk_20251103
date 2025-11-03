```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

class Enrollment(Base):
    __tablename__ = 'enrollment'
    
    # Define the primary key for the enrollment table
    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign key referencing the Student entity
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    # Foreign key referencing the Course entity
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    
    # Establish a relationship with Student and Course models
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

# Add back_populates in the associated models to establish the relationship
from src.models.student import Student
from src.models.course import Course

Student.enrollments = relationship("Enrollment", back_populates="student")
Course.enrollments = relationship("Enrollment", back_populates="course")
```