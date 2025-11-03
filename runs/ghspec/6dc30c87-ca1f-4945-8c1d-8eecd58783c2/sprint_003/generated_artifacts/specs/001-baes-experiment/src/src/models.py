```python
# src/models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()

class Course(Base):
    """
    Course model representing a course in the database.

    Attributes:
        id (int): Unique identifier for the course.
        name (str): Name of the course.
        level (str): Level of the course (e.g., beginner, intermediate, advanced).
    """
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Course name must not be null
    level = Column(String, nullable=False)  # Course level must not be null

    def __repr__(self) -> str:
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```