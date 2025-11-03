```python
# src/models/student.py

from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  # Add email field here

    def __init__(self, name: str, email: str):
        """
        Initialize a Student instance.

        :param name: The name of the student.
        :param email: The email address of the student. Must be unique and required.
        """
        self.name = name
        self.email = email
```