```python
from sqlalchemy import Column, Integer, String
from app import db

class Student(db.Model):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  # New email field added

    def __init__(self, name: str, email: str):
        # Construct a Student instance with a name and email
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Student id={self.id} name={self.name} email={self.email}>"
```