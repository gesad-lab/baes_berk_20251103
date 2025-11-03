```python
from sqlalchemy import Column, String
from app import db

class Student(db.Model):
    __tablename__ = 'students'

    id = Column(db.Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(254), nullable=False)  # Added email field to Student model

    def __repr__(self):
        return f"<Student {self.name}, Email: {self.email}>"
```