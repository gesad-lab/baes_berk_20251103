```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    """Represents a teacher entity in the application."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Teacher's name, required field
    email = Column(String, unique=True, nullable=False)  # Teacher's email, required field

    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}', email='{self.email}')>"

# Validation Logic for Teacher
def validate_teacher_input(name: str, email: str) -> None:
    """Validate the provided teacher input fields.
    
    Args:
        name (str): The name of the teacher.
        email (str): The email of the teacher.

    Raises:
        ValueError: If any of the validation checks fail.
    """
    if not name:
        raise ValueError("E001: Name field is required.")
    
    if not email:
        raise ValueError("E002: Email field is required.")
    
    if "@" not in email:
        raise ValueError("E003: Invalid email format.")
    
    # Additional validation can be added as needed
```