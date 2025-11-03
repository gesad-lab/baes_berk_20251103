```python
# src/schemas.py
from pydantic import BaseModel, EmailStr, constr

class StudentCreate(BaseModel):
    name: constr(min_length=1)  # Name should be a non-empty string
    email: EmailStr  # Email must be a valid email format

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

# Optionally, if you are updating a student's information, you might have:
class StudentUpdate(BaseModel):
    name: constr(min_length=1) = None  # Optional name field
    email: EmailStr = None  # Optional email field
```