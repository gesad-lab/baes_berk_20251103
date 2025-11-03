```python
# src/models/course.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    
    # New teacher_id field to establish relationship with Teacher model
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Foreign key reference to Teacher

    # Establish relationship to Teacher model
    teacher = relationship("Teacher", back_populates="courses")

# Note: You will need to ensure the Teacher model is defined elsewhere in your application with the back_populates set up like so:
# class Teacher(Base):
#     ...
#     courses = relationship("Course", back_populates="teacher")
```