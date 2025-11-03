```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Declare a base class for declarative class definitions
Base = declarative_base()

class Teacher(Base):
    """SQLAlchemy model for the Teacher entity, representing a teacher in the system."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each teacher
    name = Column(String, nullable=False)                        # Name of the teacher
    email = Column(String, nullable=False, unique=True)         # Unique email for authentication
    
    def __repr__(self):
        """String representation of the Teacher object."""
        return f"<Teacher(name={self.name}, email={self.email})>"
```