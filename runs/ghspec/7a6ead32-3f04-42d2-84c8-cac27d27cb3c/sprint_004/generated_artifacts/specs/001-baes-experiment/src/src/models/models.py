```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import Base, Student, Course

class StudentCourse(Base):
    """Model representing the many-to-many relationship between Students and Courses."""
    
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship(Student, back_populates="courses")
    course = relationship(Course, back_populates="students")

# Ensure you define the back_populates in Student and Course models as well:
# Example Updates (in their respective models):
# class Student(Base):
#     ...
#     courses = relationship("StudentCourse", back_populates="student")
#
# class Course(Base):
#     ...
#     students = relationship("StudentCourse", back_populates="course")
```