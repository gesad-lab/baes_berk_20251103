```python
from sqlalchemy import Column, Integer, String
from your_application import db  # Assuming you're using a common db module

class Student(db.Model):
    """Model representing a student."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field added

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"
```