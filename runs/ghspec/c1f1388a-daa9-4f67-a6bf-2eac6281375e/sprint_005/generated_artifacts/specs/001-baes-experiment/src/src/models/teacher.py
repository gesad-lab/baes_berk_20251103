```python
from sqlalchemy import Column, Integer, String
from src.db.database import Base

class Teacher(Base):
    """Teacher model definition for the database."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Teacher(name={self.name}, email={self.email})>"
```