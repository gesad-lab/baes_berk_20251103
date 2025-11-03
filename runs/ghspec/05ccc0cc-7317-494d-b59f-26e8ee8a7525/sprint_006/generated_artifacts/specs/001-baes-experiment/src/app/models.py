```python
# app/models.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    # New foreign key relationship to Teacher model
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    # Establish relationship with Teacher
    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Define relationship to courses
    courses = relationship("Course", back_populates="teacher")
```