```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a Base class for SQLAlchemy models
Base = declarative_base()

class Student(Base):
    """
    Represents a student in the 'students' table.

    Attributes:
        id (int): The unique identifier for the student, auto-incremented.
        name (str): The name of the student; must be a non-empty string.
    """
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        # String representation of the Student object for debugging
        return f"<Student(id={self.id}, name='{self.name}')>"
```