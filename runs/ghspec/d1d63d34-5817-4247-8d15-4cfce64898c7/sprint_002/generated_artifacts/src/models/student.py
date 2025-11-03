```python
# src/models/student.py

from pydantic import BaseModel, EmailStr

class Student(BaseModel):
    """Representation of a Student entity with fields for id, name, and email."""
    
    id: int  # Auto-generated, primary key
    name: str  # Required field for the student's name
    email: EmailStr  # Required field for the student's email, must be a valid email format
```