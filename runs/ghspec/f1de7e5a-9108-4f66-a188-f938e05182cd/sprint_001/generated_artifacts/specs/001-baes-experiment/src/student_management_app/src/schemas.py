```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative models
Base = declarative_base()

class Student(Base):
    """
    Represents a Student in the system, which includes an id and a name.
    
    Attributes:
        id (int): The unique identifier for the student (auto-increment).
        name (str): The name of the student (must be provided and cannot be empty).
    """
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"
```