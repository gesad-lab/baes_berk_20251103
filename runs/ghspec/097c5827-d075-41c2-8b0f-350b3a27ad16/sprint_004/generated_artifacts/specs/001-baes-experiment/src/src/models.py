```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Represents a student in the database."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    # Establish many-to-many relationship with courses through junction table
    courses = relationship('Course', secondary='student_courses', back_populates='students')

class Course(Base):
    """Represents a course in the database."""
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    # Establish many-to-many relationship with students through junction table
    students = relationship('Student', secondary='student_courses', back_populates='courses')

class StudentCourses(Base):
    """Junction table for many-to-many relationship between students and courses."""
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Optionally, add relationships for easier access if needed
    student = relationship(Student, back_populates='courses')
    course = relationship(Course, back_populates='students')
```