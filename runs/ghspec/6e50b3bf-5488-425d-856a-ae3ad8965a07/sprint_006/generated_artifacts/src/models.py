```python
# src/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base  # Assuming Base is defined in your database module

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Optional relationship to Teacher

    # Establish relationship with Teacher
    assigned_teacher = relationship("Teacher", back_populates="courses")

    def __init__(self, name, teacher_id=None):
        self.name = name
        self.teacher_id = teacher_id

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Establish relationship with Courses
    courses = relationship("Course", back_populates="assigned_teacher")

    def __init__(self, name, email):
        self.name = name
        self.email = email
```