```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    """Represents a teacher in the educational system.

    Attributes:
        id (int): The unique identifier for a teacher.
        name (str): The name of the teacher. This is a required field.
        email (str): The email of the teacher. This must be unique and is a required field.
    """

    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    def __repr__(self):
        """Return a string representation of the Teacher instance."""
        return f"<Teacher(id={self.id}, name='{self.name}', email='{self.email}')>"
```