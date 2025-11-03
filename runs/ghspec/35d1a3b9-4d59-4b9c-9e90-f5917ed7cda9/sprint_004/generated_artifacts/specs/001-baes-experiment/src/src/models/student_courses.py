```python
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourses(Base):
    """Model representing the association between Students and Courses."""
    __tablename__ = 'student_courses'
    
    # Foreign key referencing the Student entity
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    # Foreign key referencing the Course entity
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```