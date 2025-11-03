'''
Defines the Pydantic models for request validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    '''
    Pydantic model for creating a student.
    '''
    name: str
    email: EmailStr  # Added email field with validation