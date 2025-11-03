```python
from sqlalchemy import Column, Integer, ForeignKey
from app import db
from sqlalchemy.orm import relationship

class StudentCourse(db.Model):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Establish relationships to Student and Course models
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Update the Student and Course models to include relationships
from your_project.models.student import Student  # Replace with your actual import path
from your_project.models.course import Course    # Replace with your actual import path

# In Student model
Student.courses = relationship("StudentCourse", back_populates="student")

# In Course model
Course.students = relationship("StudentCourse", back_populates="course")
```