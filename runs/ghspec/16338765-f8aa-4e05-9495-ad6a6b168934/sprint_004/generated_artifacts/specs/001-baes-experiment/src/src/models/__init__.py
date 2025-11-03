```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # Define the relationship with the StudentCourse association table
    courses = relationship('StudentCourse', back_populates='student')

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    level = Column(String)
    # Define the relationship with the StudentCourse association table
    students = relationship('StudentCourse', back_populates='course')

class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    
    # Establish relationships to Student and Course models
    student = relationship('Student', back_populates='courses')
    course = relationship('Course', back_populates='students')
```