```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Course model representing a course entity in the system."""
    
    __tablename__ = 'courses'  # Name of the database table for courses
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each course
    name = Column(String, nullable=False)  # Name of the course, cannot be null
    level = Column(String, nullable=False)  # Level of the course, cannot be null
```