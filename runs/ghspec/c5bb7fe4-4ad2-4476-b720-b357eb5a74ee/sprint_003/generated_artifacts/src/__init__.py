```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Initialize the declarative base
Base = declarative_base()

class Course(Base):
    """Course model representing a course in the educational system."""
    
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-incremented primary key
    name = Column(String, nullable=False)  # Course name, required field
    level = Column(String, nullable=False)  # Course level, required field
```