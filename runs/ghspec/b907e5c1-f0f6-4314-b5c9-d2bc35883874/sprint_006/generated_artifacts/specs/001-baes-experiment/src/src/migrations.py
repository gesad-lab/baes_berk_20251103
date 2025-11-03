```python
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    
    # Foreign key to reference the Teacher entity
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    
    # Establish relationship to Teacher
    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Relationship to access associated courses
    courses = relationship("Course", back_populates="teacher")
```