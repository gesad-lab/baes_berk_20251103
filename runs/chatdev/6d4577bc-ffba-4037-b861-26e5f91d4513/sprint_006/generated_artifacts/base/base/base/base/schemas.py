'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr  # Updated to use EmailStr for validation
    class Config:
        orm_mode = True