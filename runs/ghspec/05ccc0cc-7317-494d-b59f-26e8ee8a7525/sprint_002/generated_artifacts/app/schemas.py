```python
from pydantic import BaseModel, EmailStr, Field

class StudentCreateSchema(BaseModel):
    name: str = Field(..., title="Name of the Student", description="The name of the student")
    email: EmailStr = Field(..., title="Email of the Student", description="The email address of the student. It must be a valid email format.")

class StudentResponseSchema(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # This allows compatibility with SQLAlchemy models
```