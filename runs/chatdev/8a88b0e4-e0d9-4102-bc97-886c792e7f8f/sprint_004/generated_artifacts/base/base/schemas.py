'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Use EmailStr for email validation
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Add email field
    class Config:
        orm_mode = True