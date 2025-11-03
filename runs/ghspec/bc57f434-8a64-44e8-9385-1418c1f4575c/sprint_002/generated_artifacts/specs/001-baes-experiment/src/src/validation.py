```python
from pydantic import BaseModel, EmailStr, Field

class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr  # Adding validation for email field

class StudentUpdate(BaseModel):
    email: EmailStr  # Only email can be updated

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Updated response model to include email
```