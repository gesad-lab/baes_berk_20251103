```python
# src/models/course.py

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Course model representing an academic course."""
    
    __tablename__ = 'courses'  # Define the name of the database table
    
    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for the course
    name = Column(String, nullable=False)  # Name of the course, cannot be null
    level = Column(String, nullable=False)  # Difficulty level of the course, cannot be null
```