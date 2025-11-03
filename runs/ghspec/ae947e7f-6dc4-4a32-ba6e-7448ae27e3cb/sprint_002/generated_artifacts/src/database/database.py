```python
# src/database/database.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """
    Model definition for the Student entity.

    Attributes:
        id (int): Unique identifier for the student.
        name (str): Name of the student. Required.
        email (str): Email of the student. Required and unique.
    """
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)  # Added email field

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"

# Ensure to implement further logic to create/update the database schema
# on startup accordingly if not already implemented elsewhere.
```