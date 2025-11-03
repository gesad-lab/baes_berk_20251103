```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Course(Base):  # SQLAlchemy model
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field
    level = Column(String, nullable=False)  # Required field
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Foreign key referencing Teacher
    
    # Establish relationship with Teacher model
    teacher = relationship("Teacher", back_populates="courses")

# Ensure consistency by adding a complementary relationship in the Teacher model
class Teacher(Base):  # Assuming this class exists in teacher.py
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field
    email = Column(String, nullable=False)  # Assuming an email exists
    
    # Establish reverse relationship with Course
    courses = relationship("Course", back_populates="teacher")
```