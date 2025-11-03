```python
# /src/models/teacher.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    """Model representing a Teacher entity in the database."""
    
    __tablename__ = 'teachers'  # Name of the database table

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each teacher
    name = Column(String, nullable=False)  # Name of the teacher, must not be null
    email = Column(String, nullable=False, unique=True)  # Email of the teacher, must be unique and not null

    def __repr__(self):
        """Return a string representation of the Teacher instance."""
        return f"<Teacher(id={self.id}, name='{self.name}', email='{self.email}')>"
```