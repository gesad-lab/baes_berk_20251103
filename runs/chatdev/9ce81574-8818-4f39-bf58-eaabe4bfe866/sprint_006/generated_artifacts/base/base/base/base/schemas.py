'''
Defines the Pydantic models for request validation and response serialization.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    '''
    Schema for creating a new student.
    Attributes:
    - name: str - The name of the student.
    - email: EmailStr - The email of the student (must be a valid email format).
    '''
    name: str
    email: EmailStr  # Add this line for email validation