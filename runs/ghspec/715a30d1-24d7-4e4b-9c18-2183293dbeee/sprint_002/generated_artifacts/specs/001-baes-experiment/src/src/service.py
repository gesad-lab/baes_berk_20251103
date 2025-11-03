```python
from pydantic import BaseModel, EmailStr, Field

class StudentCreateModel(BaseModel):
    name: str = Field(..., description="The name of the student, required")
    email: EmailStr = Field(..., description="The email of the student, required")

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john.doe@example.com"
            }
        }
```