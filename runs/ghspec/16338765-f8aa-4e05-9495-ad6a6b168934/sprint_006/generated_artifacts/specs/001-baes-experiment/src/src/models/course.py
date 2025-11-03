```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base  # Assuming Base is defined in a base.py file

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)

    # Add a foreign key relationship to the Teacher model
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Allow nullable for optional relationships

    # Establish the relationship to the Teacher model
    teacher = relationship("Teacher", back_populates="courses")

# Assuming Teacher class is defined somewhere else with appropriate relationship
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Establish a one-to-many relationship with Course
    courses = relationship("Course", back_populates="teacher")
```