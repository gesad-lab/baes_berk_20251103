```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()

class Student(Base):
    """
    Student model representing a student in the database.

    Attributes:
    id (int): Unique identifier for the student.
    name (str): Name of the student.
    """
    __tablename__ = 'students'  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Primary key
    name = Column(String, nullable=False)  # Student's name, cannot be null

    def __repr__(self):
        """Return a string representation of the Student object."""
        return f"<Student(id={self.id}, name='{self.name}')>"
```