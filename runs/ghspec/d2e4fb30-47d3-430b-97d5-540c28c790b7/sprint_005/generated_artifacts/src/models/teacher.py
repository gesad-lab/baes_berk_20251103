```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()

class Teacher(Base):
    """Represents a teacher in the database."""
    
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each teacher
    name = Column(String(255), nullable=False)  # Name of the teacher
    email = Column(String(255), nullable=False, unique=True)  # Email of the teacher, must be unique
```