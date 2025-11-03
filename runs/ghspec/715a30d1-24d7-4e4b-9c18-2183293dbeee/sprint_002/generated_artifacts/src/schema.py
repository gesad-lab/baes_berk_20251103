```python
# src/schema.py

from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # Added email field

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"
```