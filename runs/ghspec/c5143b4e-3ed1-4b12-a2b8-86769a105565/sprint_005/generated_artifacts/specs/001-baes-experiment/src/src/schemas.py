```python
from pydantic import BaseModel, EmailStr, Field
from typing import Any, Dict, Optional

class TeacherCreate(BaseModel):
    """
    Schema for creating a Teacher record.

    Attributes:
        name (str): The name of the teacher, required field.
        email (EmailStr): The email of the teacher, required field and must be a valid email format.
    """
    name: str = Field(..., description="The name of the teacher.")
    email: EmailStr = Field(..., description="The email of the teacher.")

class TeacherResponse(BaseModel):
    """
    Schema for returning a Teacher record.

    Attributes:
        id (str): The unique identifier for the Teacher.
        name (str): The name of the teacher.
        email (str): The email of the teacher.
        created_at (str): Timestamp of when the Teacher record was created.
    """
    id: str
    name: str
    email: str
    created_at: str

    class Config:
        orm_mode = True  # Enable ORM mode to read data as ORM objects
```
