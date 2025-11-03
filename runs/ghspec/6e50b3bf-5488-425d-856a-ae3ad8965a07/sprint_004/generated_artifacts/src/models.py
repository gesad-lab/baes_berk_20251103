```python
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class StudentCourse(Base):
    """Model representing the relationship between students and courses."""
    
    __tablename__ = 'student_course'
    
    id = Column(Integer, primary_key=True)  # Unique identifier for the relationship
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)  # Reference to Student
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)  # Reference to Course
    enrolled_at = Column(DateTime, default=datetime.utcnow)  # Timestamp for enrollment

    student = relationship("Student", back_populates="courses")  # Define relationship to Student
    course = relationship("Course", back_populates="students")  # Define relationship to Course

    def __repr__(self):
        return f"<StudentCourse(student_id={self.student_id}, course_id={self.course_id})>"
```