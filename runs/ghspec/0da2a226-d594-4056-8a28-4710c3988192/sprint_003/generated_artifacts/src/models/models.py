```python
# src/models/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """
    Course entity represents an educational course offering.
    
    Attributes:
        id (int): The unique identifier for the course.
        name (str): The name of the course, required field.
        level (str): The level of the course, required field.
    """
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Course name, required field
    level = Column(String, nullable=False)  # Course level, required field

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```