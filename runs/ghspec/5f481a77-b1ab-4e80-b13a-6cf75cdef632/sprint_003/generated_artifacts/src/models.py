```python
# src/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # Base class for the declarative model

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Course(Base):
    """Represents a Course entity in the database."""
    
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each course
    name = Column(String, nullable=False)  # Name of the course, mandatory field
    level = Column(String, nullable=False)  # Level of the course, mandatory field

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```
