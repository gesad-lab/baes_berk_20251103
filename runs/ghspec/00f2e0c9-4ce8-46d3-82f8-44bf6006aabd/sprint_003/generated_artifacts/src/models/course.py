```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()

class Course(Base):
    """Class representing a Course entity."""

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each course
    name = Column(String, nullable=False)  # Name of the course, cannot be null
    level = Column(String, nullable=False)  # Level of the course, cannot be null

    def __repr__(self):
        """Return a string representation of the Course instance."""
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}')>"
```