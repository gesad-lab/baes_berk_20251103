```python
# models.py
from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)  # Unique identifier for each student
    name = Column(String, nullable=False)     # Student's name; cannot be null

    def __repr__(self):
        return f"<Student(name='{self.name}')>"
```