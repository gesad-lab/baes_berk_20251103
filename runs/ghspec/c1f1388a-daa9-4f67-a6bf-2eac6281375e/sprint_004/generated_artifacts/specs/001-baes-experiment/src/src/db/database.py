```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

class Enrollment(Base):
    __tablename__ = 'enrollment'

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)

    # Establishing relationships to the Student and Course models
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

# Update Student model to include the relationship
from src.models.student import Student
Student.enrollments = relationship("Enrollment", back_populates="student")

# Update Course model to include the relationship
from src.models.course import Course
Course.enrollments = relationship("Enrollment", back_populates="course")
```