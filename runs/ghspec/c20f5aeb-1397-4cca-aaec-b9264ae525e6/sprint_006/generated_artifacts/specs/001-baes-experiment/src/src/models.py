```python
# src/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    
    # Adding a foreign key relationship to the Teacher entity
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    
    # Establishing the relationship with the Teacher model
    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Back reference to courses linked to the teacher
    courses = relationship("Course", back_populates="teacher")
```
