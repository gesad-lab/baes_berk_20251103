```python
from sqlalchemy import Column, Integer, String
from src.database import Base  # Assuming Base is imported from a module where your SQLAlchemy models Base is defined

class Teacher(Base):
    """Model representing a teacher in the educational system."""
    
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}', email='{self.email}')>"
```