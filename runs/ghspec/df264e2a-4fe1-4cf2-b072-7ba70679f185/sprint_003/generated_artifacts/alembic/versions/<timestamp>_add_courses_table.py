```python
# app/models/course.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Course model represents a course in the educational system."""

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field for course name
    level = Column(String, nullable=False)  # Required field for course level

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}')>"
```