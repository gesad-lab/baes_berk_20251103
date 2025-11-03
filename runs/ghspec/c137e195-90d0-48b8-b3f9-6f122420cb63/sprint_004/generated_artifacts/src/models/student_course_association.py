```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class StudentCourseAssociation(Base):
    """Junction model for associating students with courses."""
    
    __tablename__ = "student_course_association"

    id = Column(Integer, primary_key=True, index=True)  # Primary key for the junction table
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)  # Foreign key from students table
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)  # Foreign key from courses table

    # Relationships to access related student and course objects
    student = relationship("Student", back_populates="courses")  # Associate with Student model
    course = relationship("Course", back_populates="students")    # Associate with Course model

    def __repr__(self):
        return f"<StudentCourseAssociation(student_id={self.student_id}, course_id={self.course_id})>"
```