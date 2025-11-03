```python
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Add foreign key reference to Teacher

    teacher = relationship("Teacher", back_populates="courses")


class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    
    courses = relationship("Course", back_populates="teacher")  # Relationship definition
```