```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Teacher(Base):
    """Representation of a Teacher in the system."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Teacher's name, must be provided
    email = Column(String, nullable=False, unique=True)  # Teacher's email, must be unique
    created_at = Column(DateTime, default=datetime.utcnow)  # Record creation timestamp
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Record last update timestamp
```