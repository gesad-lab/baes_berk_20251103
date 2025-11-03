```python
# src/models.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    
    # New field for teacher assignment
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    # Establish a relationship with the Teacher model
    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Relationship to access courses assigned to this teacher
    courses = relationship("Course", back_populates="teacher")
```