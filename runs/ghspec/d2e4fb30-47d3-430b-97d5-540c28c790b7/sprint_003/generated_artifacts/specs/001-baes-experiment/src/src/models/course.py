```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()

class Course(Base):
    """Database model for a Course."""

    __tablename__ = 'courses'
    
    # Auto-generated primary key
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Name of the course, must be provided
    name = Column(String(255), nullable=False)
    
    # Level of the course, must be provided
    level = Column(String(255), nullable=False)

    def __repr__(self):
        """Return a string representation of the Course."""
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}')>"
```