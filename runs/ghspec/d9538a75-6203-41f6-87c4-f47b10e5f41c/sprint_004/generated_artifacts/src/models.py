```python
# src/models.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    courses = relationship('StudentCourses', back_populates='student')

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)

class StudentCourses(Base):
    """Associates students with their enrolled courses."""
    
    __tablename__ = 'student_courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

    student = relationship('Student', back_populates='courses')
    course = relationship('Course')  # Assuming Course model exists and is properly defined

# Ensure all tables are created in the database
def setup_database(engine):
    """Create the tables in the database if they do not already exist."""
    Base.metadata.create_all(engine)

# This setup_database function should be called at application startup
# or when initializing the database to ensure the virtual environment is ready and the database schema is up-to-date.
```