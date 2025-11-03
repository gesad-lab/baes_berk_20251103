```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(String, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Adding the foreign key for the Teacher entity

    teacher = relationship("Teacher", back_populates="courses")  # Establish relationship with Teacher

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)

    courses = relationship("Course", back_populates="teacher")  # Establish reverse relationship to Course
```