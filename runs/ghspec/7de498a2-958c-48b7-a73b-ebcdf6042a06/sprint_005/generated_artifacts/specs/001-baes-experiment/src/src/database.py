```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    """Represents a Teacher entity in the database."""
    
    __tablename__ = 'teachers'  # Database table name

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for each teacher
    name = Column(String, nullable=False)  # Teacher's name (required)
    email = Column(String, nullable=False, unique=True)  # Teacher's email (required)

    def __repr__(self):
        return f"<Teacher(name={self.name}, email={self.email})>"
```