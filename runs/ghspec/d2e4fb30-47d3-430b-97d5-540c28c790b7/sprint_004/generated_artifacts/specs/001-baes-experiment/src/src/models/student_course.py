```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class StudentCourse(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Establish relationships with Student and Course models
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Note: Ensure that you also have the following relationships defined in the respective models:

# In `student.py`:
# class Student(Base):
#     ...
#     courses = relationship("StudentCourse", back_populates="student")

# In `course.py`:
# class Course(Base):
#     ...
#     students = relationship("StudentCourse", back_populates="course")
```