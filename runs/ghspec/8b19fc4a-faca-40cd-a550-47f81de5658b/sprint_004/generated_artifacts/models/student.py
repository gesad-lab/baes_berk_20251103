```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Student model to store student information and their associated courses."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    # Relationship for courses - one student can have multiple courses
    courses = relationship("Course", secondary="student_courses", back_populates="students")

class Course(Base):
    """Course model to store course information."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    # Relationship for students - one course can have multiple students
    students = relationship("Student", secondary="student_courses", back_populates="courses")

# Join table for many-to-many relationship between students and courses
class StudentCourses(Base):
    """Table to associate students with courses."""
    
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```