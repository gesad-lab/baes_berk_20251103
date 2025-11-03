```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field
    email = Column(String, nullable=False)  # New required field

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"
```