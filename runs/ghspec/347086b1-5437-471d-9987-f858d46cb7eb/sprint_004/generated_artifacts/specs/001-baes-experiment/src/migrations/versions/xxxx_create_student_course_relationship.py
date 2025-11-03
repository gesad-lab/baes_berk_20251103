```python
# src/models/student.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    # Establishing a many-to-many relationship with Course through the student_courses association table
    courses = relationship(
        "Course",
        secondary="student_courses",
        back_populates="students"
    )

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    level = Column(String)

    # Establishing a many-to-many relationship with Student through the student_courses association table
    students = relationship(
        "Student",
        secondary="student_courses",
        back_populates="courses"
    )
```