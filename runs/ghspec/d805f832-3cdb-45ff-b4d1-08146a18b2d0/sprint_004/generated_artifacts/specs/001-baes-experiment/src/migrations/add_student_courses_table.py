```python
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from models import Base

# Junction table for many-to-many relationship between Student and Course
student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    """Student model representing a student in the educational framework.

    Attributes:
        id (int): The unique identifier for the student.
        name (str): The name of the student (required).
        courses (relationship): List of courses associated with the student.
    """
    
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    # Establish a relationship to access courses associated with the student
    courses = relationship('Course', secondary=student_courses, back_populates='students')


class Course(Base):
    """Course model representing a course in the educational framework.

    Attributes:
        id (int): The unique identifier for the course.
        name (str): The name of the course (required).
        students (relationship): List of students enrolled in the course.
    """
    
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # Establish a relationship to access students associated with the course
    students = relationship('Student', secondary=student_courses, back_populates='courses')
```