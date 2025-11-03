'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Add email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr  # Add email field
    class Config:
        orm_mode = True