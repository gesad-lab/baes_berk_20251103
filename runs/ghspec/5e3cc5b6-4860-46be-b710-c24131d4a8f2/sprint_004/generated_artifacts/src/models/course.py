```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Establish a relationship with the Student through StudentCourse
    students = relationship("StudentCourse", back_populates="course")

class StudentCourse(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Define relationships
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Update the Student model to include the relationship
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Establish the relationship with courses through StudentCourse
    courses = relationship("StudentCourse", back_populates="student")
```