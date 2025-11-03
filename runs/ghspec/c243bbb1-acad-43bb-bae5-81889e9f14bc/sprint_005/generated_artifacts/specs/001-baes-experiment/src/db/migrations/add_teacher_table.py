```python
# db/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    """Represents a teacher in the educational management system."""
    
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        """Return a string representation of the Teacher."""
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"
```