```python
# src/models/course.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New foreign key column

    # Establishing a relationship with the Teacher model
    teacher = relationship("Teacher", back_populates="courses")  # Adding relationship with Teacher

# src/models/teacher.py (for reference)

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.db.database import Base

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    # Establishing a relationship with the Course model
    courses = relationship("Course", back_populates="teacher")  # Adding relationship with Course
```