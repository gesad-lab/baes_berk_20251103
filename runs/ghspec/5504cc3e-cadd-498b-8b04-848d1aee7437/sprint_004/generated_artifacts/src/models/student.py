```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base  # Assuming there's a base module where Base is defined

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # Assuming a name field exists

    # Relationship to StudentCourse
    courses = relationship("StudentCourse", back_populates="student")

class StudentCourse(Base):
    __tablename__ = 'student_course'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)  # Assuming a title field exists
    
    # Relationship to StudentCourse
    students = relationship("StudentCourse", back_populates="course")
```