'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
    email: str  # Add this line
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Add this line
    class Config:
        orm_mode = True