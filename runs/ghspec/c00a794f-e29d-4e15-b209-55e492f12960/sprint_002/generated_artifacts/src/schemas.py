```python
# src/schemas.py

from pydantic import BaseModel, EmailStr, Field, constr, validator
from typing import Optional

class StudentSchema(BaseModel):
    name: constr(min_length=1)  # Name must be at least one character
    email: EmailStr  # Email is validated using Pydantic's built-in Email validation

    @validator('email', always=True)
    def validate_email(cls, value):
        if not value:
            raise ValueError('Email is required.')
        return value

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com"
            }
        }
```
