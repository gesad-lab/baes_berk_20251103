```python
from sqlalchemy import Column, Integer, String
from src.database import Base  # Assuming Base is defined in the database module

class Teacher(Base):
    """Model representing a Teacher entity in the educational system."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each teacher
    name = Column(String, nullable=False)  # Name of the teacher, cannot be null
    email = Column(String, nullable=False, unique=True)  # Email of the teacher, must be unique and cannot be null
```