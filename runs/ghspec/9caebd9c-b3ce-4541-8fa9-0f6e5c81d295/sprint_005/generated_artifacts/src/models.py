```python
# src/models.py
from sqlalchemy import Column, Integer, String
from database import Base

class Teacher(Base):
    """
    Teacher Model

    This class represents the teacher entity in the database. It includes fields for the teacher's
    ID, name, and email, which are essential for the management of teacher data.
    """
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each teacher
    name = Column(String, nullable=False)  # Name of the teacher
    email = Column(String, unique=True, nullable=False)  # Email address of the teacher, must be unique

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"
```