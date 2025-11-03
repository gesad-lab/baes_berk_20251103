```python
from sqlalchemy import Column, Integer, String
from src.database import Base

class Course(Base):
    """Represents a Course entity in the database.

    Attributes:
        id: Unique identifier for each course (integer).
        name: The name of the course (string, required).
        level: The level of the course (string, required).
    """
    
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```