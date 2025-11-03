```python
# src/models/student.py

from sqlalchemy import Column, Integer, String
from app import db

class Student(db.Model):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # Adding the new email attribute

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Student(name='{self.name}', email='{self.email}')>"
```