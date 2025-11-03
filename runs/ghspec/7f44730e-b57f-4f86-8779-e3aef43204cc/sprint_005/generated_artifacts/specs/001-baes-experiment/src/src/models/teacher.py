```python
# src/models/teacher.py
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    """Represents a Teacher entity in the database."""
    
    __tablename__ = 'teachers'

    id = Column(String, primary_key=True, index=True)  # Auto-generated ID
    name = Column(String, nullable=False)  # Required teacher name
    email = Column(String, nullable=False, unique=True)  # Required teacher email (must be unique)

    def __repr__(self):
        return f"<Teacher(name={self.name}, email={self.email})>"
```