```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourses(Base):
    """Model representing the many-to-many relationship between students and courses."""
    
    __tablename__ = 'student_courses'
    
    # Foreign key reference to the Student entity
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    # Foreign key reference to the Course entity
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    def __repr__(self):
        """Provide a string representation of the StudentCourses object for debugging."""
        return f"<StudentCourses(student_id={self.student_id}, course_id={self.course_id})>"
```