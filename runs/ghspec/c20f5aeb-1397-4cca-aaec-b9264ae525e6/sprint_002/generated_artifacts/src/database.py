```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from database import Base

class Student(Base):
    """Represents a student in the database."""
    
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Student name, required
    email = Column(String, nullable=False)  # New email field added, required
```