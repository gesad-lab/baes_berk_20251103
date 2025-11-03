'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    '''
    Schema for creating a new student.
    '''
    name: str
class StudentResponse(BaseModel):
    '''
    Schema for student response.
    '''
    id: int
    name: str
    class Config:
        orm_mode = True