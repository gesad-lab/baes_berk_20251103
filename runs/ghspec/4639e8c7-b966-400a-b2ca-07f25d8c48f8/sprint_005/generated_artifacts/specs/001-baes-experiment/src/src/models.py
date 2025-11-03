```python
from sqlalchemy import Column, Integer, String, UniqueConstraint
from src.models import Base  # Assuming Base is defined as part of the SQLAlchemy setup

class Teacher(Base):
    """Represents a teacher in the Student Management System."""

    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)  # Unique identifier for each teacher
    name = Column(String, nullable=False)     # Teacher's full name
    email = Column(String, nullable=False, unique=True)  # Teacher's email address, must be unique

    __table_args__ = (UniqueConstraint('email', name='uq_teacher_email'),)  # Ensure email is unique

    def __repr__(self):
        """Provide a string representation of the Teacher instance."""
        return f"<Teacher(name={self.name}, email={self.email})>"
```