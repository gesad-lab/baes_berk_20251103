```python
# src/models/teacher.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    """ORM model for Teacher entity representing educational staff in the system."""
    
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Name of the teacher, required field
    email = Column(String, unique=True, nullable=False)  # Unique email of the teacher, required field

    def __repr__(self):
        """Return a string representation of the Teacher object."""
        return f"<Teacher(id={self.id}, name='{self.name}', email='{self.email}')>"
```