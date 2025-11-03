```python
from sqlalchemy import Column, Integer, String
from api import db

class Teacher(db.Model):
    """Teacher model for storing information about teachers."""
    
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-incremented primary key
    name = Column(String, nullable=False)  # Required name field
    email = Column(String, nullable=False, unique=True)  # Required email field with format validation

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"
```