```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Add teacher_id as a ForeignKey

    # Define relationship to the Teacher model
    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    # Define relationship to the Course model
    courses = relationship("Course", back_populates="teacher")
```