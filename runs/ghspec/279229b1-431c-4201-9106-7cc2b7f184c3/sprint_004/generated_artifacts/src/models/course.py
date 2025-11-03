```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    
    # Establish a relationship to the StudentCourse junction table
    students = relationship("StudentCourse", back_populates="course")

# Ensure that the newly added relationship in the StudentCourse model can reference back
class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Ensure the existing Student model is also modified to include relationship
# This part assumes that the Student model is defined in another file
# Modify src/models/student.py accordingly to add the back_populates for courses
```