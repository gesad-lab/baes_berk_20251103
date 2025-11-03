```python
from pydantic import BaseModel, EmailStr

class TeacherCreate(BaseModel):
    """
    Schema for creating a new teacher.
    
    Attributes:
    - name (str): The name of the teacher (required).
    - email (EmailStr): The email of the teacher (required and must be a valid email format).
    """
    name: str
    email: EmailStr

class TeacherResponse(BaseModel):
    """
    Schema for the response after creating or retrieving a teacher.
    
    Attributes:
    - id (int): Unique identifier for the teacher.
    - name (str): The name of the teacher.
    - email (EmailStr): The email of the teacher.
    """
    id: int
    name: str
    email: EmailStr
```