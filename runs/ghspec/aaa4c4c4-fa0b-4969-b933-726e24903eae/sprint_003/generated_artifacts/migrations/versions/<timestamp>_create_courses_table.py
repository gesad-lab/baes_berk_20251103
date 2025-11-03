```python
from sqlalchemy import Column, Integer, String
from database import Base

class Course(Base):
    """Course model to represent a course in the system."""
    
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Name of the course, required field
    level = Column(String, nullable=False)  # Level of the course, required field
```