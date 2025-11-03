'''
Defines the Pydantic model for request validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
    email: str  # New email field added