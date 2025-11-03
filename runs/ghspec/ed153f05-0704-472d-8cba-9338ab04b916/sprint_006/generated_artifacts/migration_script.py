```python
# File: src/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Teacher(Base):
    """Model representing a teacher."""
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    courses = relationship('Course', back_populates='teacher')

class Course(Base):
    """Model representing a course."""
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    course_name = Column(String, nullable=False)
    
    # New foreign key to establish relationship with Teacher
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    
    # Establish relationship for easier access to Teacher data
    teacher = relationship('Teacher', back_populates='courses')
```