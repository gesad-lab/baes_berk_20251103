'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # New email field added with validation
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # New email field added to response
    class Config:
        orm_mode = True