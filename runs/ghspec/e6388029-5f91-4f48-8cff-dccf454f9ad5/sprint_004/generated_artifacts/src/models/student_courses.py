```python
from sqlalchemy import Column, Integer, ForeignKey
from src.database import Base

class StudentCourses(Base):
    """Association table to link students with their enrolled courses."""
    
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    def __repr__(self):
        return f"<StudentCourses(student_id={self.student_id}, course_id={self.course_id})>"
```