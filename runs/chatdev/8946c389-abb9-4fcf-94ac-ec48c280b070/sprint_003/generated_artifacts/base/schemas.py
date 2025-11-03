'''
Defines the Pydantic models for the Student entity.
'''
from pydantic import BaseModel
class StudentBase(BaseModel):
    name: str
    email: str  # Add email field
class StudentCreate(StudentBase):
    pass
class StudentResponse(StudentBase):
    id: int
    class Config:
        orm_mode = True