'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True