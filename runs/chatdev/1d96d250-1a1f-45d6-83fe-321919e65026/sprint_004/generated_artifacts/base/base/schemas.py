'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    '''
    Schema for creating a new student.
    '''
    name: str
    email: str  # Add email field
class StudentResponse(BaseModel):
    '''
    Schema for returning student data.
    '''
    id: int
    name: str
    email: str  # Add email field
    class Config:
        orm_mode = True