```python
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.db import Base  # Assuming Base is defined in your database setup

class StudentCourse(Base):
    """Mapping class for the association between Students and Courses."""
    
    __tablename__ = 'student_course'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship('Student', backref='course_associations')
    course = relationship('Course', backref='student_associations')

    def __repr__(self):
        """Return a string representation of the StudentCourse association."""
        return f"<StudentCourse(student_id={self.student_id}, course_id={self.course_id})>"
```