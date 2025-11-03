'''
Defines the Pydantic model for the Student entity.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
    email: str  # Added email field