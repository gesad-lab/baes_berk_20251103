```python
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

# Define the association table for many-to-many relationship between students and courses
student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True),
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    # Relationship to access courses associated with a student
    courses = relationship("Course", secondary=student_courses, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    
    # Relationship to access students associated with a course
    students = relationship("Student", secondary=student_courses, back_populates="courses")
```