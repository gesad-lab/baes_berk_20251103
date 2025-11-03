'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
    email: str  # Add email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Include email in response model
    class Config:
        orm_mode = True