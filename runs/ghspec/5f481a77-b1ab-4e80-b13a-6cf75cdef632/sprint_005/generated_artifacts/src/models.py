```python
from sqlalchemy import Column, Integer, String
from src.db import db

class Teacher(db.Model):
    """Model representing a Teacher entity."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Teacher {self.name} - {self.email}>'
```