```python
# src/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Course model representing course data in the database."""
    
    __tablename__ = 'courses'  # Table name in the database

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each course
    name = Column(String, nullable=False)  # Name of the course, must be provided
    level = Column(String, nullable=False)  # Level of the course, must be provided

    def __repr__(self):
        """Return a string representation of the Course model."""
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```