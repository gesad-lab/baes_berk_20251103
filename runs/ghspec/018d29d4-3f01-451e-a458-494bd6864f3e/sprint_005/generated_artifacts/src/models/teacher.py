```python
from sqlalchemy import Column, String, Integer
from src.database import Base  # Assuming Base is imported from a database module

class Teacher(Base):
    """Model representing a Teacher entity in the database."""
    
    __tablename__ = 'teachers'  # Name of the table in the database
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each teacher
    name = Column(String, nullable=False)  # Teacher's name (required field)
    email = Column(String, nullable=False, unique=True)  # Teacher's email (required field, must be unique)

    def __repr__(self):
        """String representation of the Teacher instance."""
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"
```