```python
# src/models.py
from sqlalchemy import Column, Integer, String
from database import Base

class Course(Base):
    """
    Course model representing an educational course.
    
    Attributes:
        id (int): The unique identifier for the course.
        name (str): The name of the course.
        level (str): The level of the course (e.g., beginner, intermediate, advanced).
    """
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Name of the course
    level = Column(String, nullable=False)  # Level of the course

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}')>"
```