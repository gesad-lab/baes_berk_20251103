```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    # Establish a many-to-many relationship with Course through StudentCourses
    courses = relationship('Course', secondary='student_courses', back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    # Establish a many-to-many relationship with Student through StudentCourses
    students = relationship('Student', secondary='student_courses', back_populates='courses')

class StudentCourses(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

# Note: Ensure appropriate indexing and linking, and any additional fields as
# necessary based on future requirements (like timestamps).
```