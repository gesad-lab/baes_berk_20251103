```python
from sqlalchemy import Column, Integer, String
from src.database import Base

class Course(Base):
    """
    Course model representing the course entity in the database.

    Attributes:
        id (int): Unique identifier for the course (auto-generated).
        name (str): The name of the course (required).
        level (str): The educational level of the course (required).
    """
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Required
    level = Column(String, nullable=False)  # Required
```