'''
Defines Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Add this line for email validation
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Add this line to include email in the response
    class Config:
        orm_mode = True