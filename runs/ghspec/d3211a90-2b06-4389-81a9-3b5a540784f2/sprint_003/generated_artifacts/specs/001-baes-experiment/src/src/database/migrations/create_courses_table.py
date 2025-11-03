```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """
    Course model representing a course in the application.

    Attributes:
        id (int): The unique identifier for the course (primary key).
        name (str): The name of the course (required).
        level (str): The level of the course (required).
    """
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field
    level = Column(String, nullable=False)  # Required field
```