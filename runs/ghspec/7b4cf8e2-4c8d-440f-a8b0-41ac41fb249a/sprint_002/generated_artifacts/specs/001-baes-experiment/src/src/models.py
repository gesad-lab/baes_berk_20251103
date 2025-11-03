```python
# src/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Represents a student entity in the database."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New required email field

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"
    
    # Additional methods can be added as needed for business logic.

# Migration logic will need to be handled in a separate migration script
```