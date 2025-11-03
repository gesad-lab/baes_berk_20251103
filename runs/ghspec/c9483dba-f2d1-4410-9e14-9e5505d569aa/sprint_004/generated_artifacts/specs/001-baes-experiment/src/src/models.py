```python
# src/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from base import Base  # Assuming you have a Base class for your SQLAlchemy models

# Association table between students and courses
student_courses = Table('student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    """Represents a student in the system."""

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Many-to-many relationship with Course
    courses = relationship('Course', secondary=student_courses, back_populates='students')

class Course(Base):
    """Represents a course in the system."""

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    # Many-to-many relationship with Student
    students = relationship('Student', secondary=student_courses, back_populates='courses')
```