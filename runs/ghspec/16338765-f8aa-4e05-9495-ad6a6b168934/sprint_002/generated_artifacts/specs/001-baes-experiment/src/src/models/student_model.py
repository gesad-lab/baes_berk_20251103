```python
from pydantic import BaseModel, EmailStr  # Import EmailStr for email validation

class StudentCreate(BaseModel):
    name: str  # Name of the student
    email: EmailStr  # Email is now a required field for student creation

class StudentResponse(BaseModel):
    id: int  # Unique identifier for the student
    name: str  # Name of the student
    email: str  # Email of the student for contact purposes

class StudentUpdate(BaseModel):
    name: str = None  # Optional update for name
    email: EmailStr = None  # Optional update for email
```