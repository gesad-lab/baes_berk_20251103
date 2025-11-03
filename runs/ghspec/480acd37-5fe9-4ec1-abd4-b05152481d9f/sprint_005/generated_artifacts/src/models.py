```python
from sqlalchemy import Column, Integer, String, UniqueConstraint
from .database import Base  # Import the Base model for SQLAlchemy

class Teacher(Base):
    """Model representing a teacher in the system."""
    
    __tablename__ = 'teachers'  # Define the table name

    id = Column(Integer, primary_key=True, index=True)  # Primary key of the teacher
    name = Column(String, nullable=False)  # Teacher's name, cannot be null
    email = Column(String, nullable=False, unique=True)  # Teacher's email, must be unique

    __table_args__ = (UniqueConstraint('email', name='uq_email'),)  # Ensure email uniqueness at the database level
```