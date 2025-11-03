'''
Defines the Pydantic models for request validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    '''
    Pydantic model for creating a student.
    '''
    name: str