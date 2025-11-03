```python
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Enrollment(Base):
    """Model representing the enrollment of a student in a course."""
    
    __tablename__ = 'enrollments'
    
    id = Column(String, primary_key=True)
    student_id = Column(String, ForeignKey('students.id'), nullable=False)
    course_id = Column(String, ForeignKey('courses.id'), nullable=False)
    
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id})>"
```