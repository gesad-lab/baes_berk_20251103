```python
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Relationship to courses
    courses = relationship("Course", back_populates="teacher")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New foreign key column

    # Relationship to teacher
    teacher = relationship("Teacher", back_populates="courses")

    created_at = Column(DateTime, default=datetime.utcnow)  # Existing attribute
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Existing attribute
```