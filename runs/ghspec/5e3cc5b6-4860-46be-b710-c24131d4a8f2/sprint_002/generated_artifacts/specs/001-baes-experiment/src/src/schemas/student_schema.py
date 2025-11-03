```python
from pydantic import BaseModel, constr, EmailStr

class StudentCreate(BaseModel):
    name: constr(min_length=1, max_length=100)  # Required name field with length validation
    email: EmailStr  # New field added with Email validation

class StudentResponse(BaseModel):
    id: int  # Student ID
    name: str  # Student name
    email: str  # Include email in response
```