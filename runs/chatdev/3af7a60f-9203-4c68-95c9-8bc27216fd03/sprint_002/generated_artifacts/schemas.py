'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Updated to use EmailStr for email validation
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field for response
    class Config:
        orm_mode = True