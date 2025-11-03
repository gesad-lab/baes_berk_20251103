```python
from sqlalchemy import Column, Integer, String
from database.db import Base

class Student(Base):
    """Represents a student in the system."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each student
    name = Column(String, nullable=False)  # Required name field for the student
```