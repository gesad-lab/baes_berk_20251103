```python
# src/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # Assume Base is defined in your SQLAlchemy setup

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Add foreign key to Teacher model

    # Relationship to Teacher model
    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    # Relationship to Course model
    courses = relationship("Course", back_populates="teacher")
```