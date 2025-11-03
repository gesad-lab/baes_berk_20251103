```python
# src/models/teacher.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

class Teacher(Base):
    """Teacher model representing a teacher in the system."""
    
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    # Define a one-to-many relationship: one teacher can teach many courses
    courses = relationship("Course", back_populates="teacher")

# Update to ensure Course model references the Teacher model
# Assuming Course model is defined in src/models/course.py
from src.models.course import Course

Course.teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Add foreign key to Course
```