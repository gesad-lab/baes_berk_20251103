```python
# src/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Course model represents the course entity in the database."""
    
    __tablename__ = 'courses'

    # Unique identifier for the course
    id = Column(Integer, primary_key=True, autoincrement=True)
    # The name of the course, must be a non-empty string
    name = Column(String, nullable=False)
    # The level of the course, must be a non-empty string
    level = Column(String, nullable=False)
```