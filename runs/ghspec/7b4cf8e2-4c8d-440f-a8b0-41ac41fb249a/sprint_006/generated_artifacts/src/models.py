```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Updated to include teacher_id

    # Relationship to the Teacher model
    teacher = relationship("Teacher", back_populates="courses")  # Assuming Teacher class has courses relationship

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Relationship to the Course model
    courses = relationship("Course", back_populates="teacher")  # Enables access to courses from Teacher
```