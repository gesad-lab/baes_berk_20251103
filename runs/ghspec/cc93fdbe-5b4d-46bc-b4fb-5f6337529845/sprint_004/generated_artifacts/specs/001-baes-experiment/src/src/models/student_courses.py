```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourses(Base):
    """Model representing the many-to-many relationship between students and courses."""
    
    __tablename__ = 'student_courses'

    # Foreign key referencing the student ID
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    
    # Foreign key referencing the course ID
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```