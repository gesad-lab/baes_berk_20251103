```python
# models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for declarative class definitions
Base = declarative_base()

class Student(Base):
    """Represents the Student entity in the database."""
    
    __tablename__ = 'students'  # Set the table name in the database

    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-incrementing ID
    name = Column(String, nullable=False)  # Required name field

    def __repr__(self):
        """Return a string representation of the Student object."""
        return f"<Student(id={self.id}, name={self.name})>"
```