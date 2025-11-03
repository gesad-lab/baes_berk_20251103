```python
# File: src/models/teacher.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    # Relationship to link Teacher to Courses
    courses = relationship("Course", back_populates="teacher")

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    # Establishing the relationship with Teacher
    teacher = relationship("Teacher", back_populates="courses")
```