```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    # Back-reference to courses
    courses = relationship("Course", back_populates="teacher")

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    
    # New foreign key reference to the Teacher
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    teacher = relationship("Teacher", back_populates="courses")

    # Additional fields can be defined here as required
```