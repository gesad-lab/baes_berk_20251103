```python
# This file has not yet been populated with code.
# It is intended to define the Student model using SQLAlchemy.

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Creating a declarative base for SQLAlchemy models.
Base = declarative_base()

class Student(Base):
    """
    Represents a student entity in the database.

    Attributes:
        id (int): The unique identifier for the student.
        name (str): The name of the student. This field cannot be null.
    """
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
```