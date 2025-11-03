```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base class for the SQLAlchemy models
Base = declarative_base()

class Course(Base):
    """Course model to represent a course entity in the database."""
    
    __tablename__ = 'courses'
    
    # Auto-generated primary key for each course
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Name of the course, this field is required
    name = Column(String, nullable=False)
    # Level of the course, this field is required
    level = Column(String, nullable=False)
```