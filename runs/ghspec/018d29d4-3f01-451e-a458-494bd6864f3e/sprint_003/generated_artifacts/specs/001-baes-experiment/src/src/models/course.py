```python
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Course model to represent a course entity in the database."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the course
    name = Column(String, nullable=False)  # Name of the course, required field
    level = Column(String, nullable=False)  # Level of the course, required field

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}')>"
```