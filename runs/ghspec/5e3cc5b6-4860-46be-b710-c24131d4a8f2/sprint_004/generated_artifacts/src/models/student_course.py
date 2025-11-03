```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database.database import Base

class StudentCourse(Base):
    """Defines the relationship between Students and Courses."""
    
    __tablename__ = 'student_course'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-generated primary key
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)  # Foreign key to Student
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)  # Foreign key to Course

    # Define relationships for easier access
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

    def __repr__(self):
        return f"<StudentCourse(student_id={self.student_id}, course_id={self.course_id})>"
```
