```python
from pydantic import BaseModel, EmailStr, constr

class StudentCreate(BaseModel):
    name: constr(min_length=1)  # Requiring at least one character for the name
    email: EmailStr  # EmailStr will validate the email format

    class Config:
        orm_mode = True  # Enables compatibility with ORM models, such as SQLAlchemy

class StudentResponse(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True
```