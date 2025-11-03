```python
# src/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database import Base

class Teacher(Base):
    """Model representing a teacher in the system."""
    
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each teacher
    name = Column(String(255), nullable=False)                   # Teacher's name, cannot be null
    email = Column(String(255), nullable=False, unique=True)     # Teacher's email, must be unique and cannot be null

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"
```