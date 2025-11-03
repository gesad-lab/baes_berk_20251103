```python
# src/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

# New Course class definition
class Course(Base):
    """Course model representing a course entity in the system."""
    
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Course name, should not be null
    level = Column(String, nullable=False)  # Course level, should not be null

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```