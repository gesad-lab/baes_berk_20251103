```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Model for representing a Student entity."""
    
    __tablename__ = 'students'
    
    # Unique identifier for the student
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Name of the student, cannot be null
    name = Column(String, nullable=False)

    def __repr__(self):
        """String representation of the Student object for debugging."""
        return f"<Student(id={self.id}, name='{self.name}')>"
```