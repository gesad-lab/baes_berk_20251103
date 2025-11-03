```python
from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    """
    Pydantic model for creating a new student.
    Includes fields for name and email.
    """
    name: str
    email: EmailStr  # This field requires a valid email format

class StudentResponse(BaseModel):
    """
    Pydantic model for responding with student information.
    Includes fields for name and email.
    """
    id: int
    name: str
    email: str  # Email field included for response
```