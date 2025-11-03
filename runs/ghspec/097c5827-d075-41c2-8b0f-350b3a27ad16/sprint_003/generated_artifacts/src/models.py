```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Course model represents the structure of Course data in the database."""

    __tablename__ = 'courses'

    # Auto-incrementing primary key for each course
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Name of the course, required field
    name = Column(String, nullable=False)
    # Level of the course, required field
    level = Column(String, nullable=False)

    def __repr__(self):
        """Return a string representation of the Course instance."""
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}')>"
```