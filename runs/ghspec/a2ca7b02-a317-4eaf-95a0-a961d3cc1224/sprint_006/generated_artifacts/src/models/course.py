```python
# File: src/models/course.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    
    # New relationship field to store the associated teacher's ID
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  
    # Establish relationship to Teacher model
    teacher = relationship("Teacher", back_populates="courses")  

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Reverse relationship for Course
    courses = relationship("Course", back_populates="teacher")  
```