```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Represents a student in the database."""

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=True)  # New field to store student email

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age}, email='{self.email}')>"
```