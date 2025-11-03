```python
# src/models/enrollment_model.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base  # Assuming there is a Base for declarative base from SQLAlchemy

class Enrollment(Base):
    """Model representing the enrollment of a student in a course."""
    
    __tablename__ = 'enrollments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-incrementing primary key
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)  # Foreign key to Student
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)  # Foreign key to Course

    # Relationships
    student = relationship("Student", back_populates="enrollments")  # Linking to Student model
    course = relationship("Course", back_populates="enrollments")    # Linking to Course model

    def __repr__(self):
        """String representation of the Enrollment model."""
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id})>"
```

### Changes Made:
- Created a new `Enrollment` model to represent the many-to-many relationship between students and courses.
- Used SQLAlchemy's ORM features to define foreign keys linking to the existing `Student` and `Course` models.
- Established relationships for easier access to related objects.
- Followed the existing coding structure and style used in the previous models.