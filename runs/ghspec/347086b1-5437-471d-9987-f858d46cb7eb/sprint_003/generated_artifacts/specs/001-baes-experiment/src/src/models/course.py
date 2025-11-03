```python
# src/models/course.py

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# Define the base class for models
Base = declarative_base()

class Course(Base):
    """
    Course model to represent courses offered in the system.

    Attributes:
    - id (int): The primary key for the course.
    - name (str): The name of the course (required).
    - level (str): The level of the course (required).
    """
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}')>"
```