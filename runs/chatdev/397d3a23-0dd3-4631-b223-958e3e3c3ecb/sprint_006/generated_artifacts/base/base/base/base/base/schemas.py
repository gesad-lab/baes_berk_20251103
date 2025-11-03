'''
Defines the Pydantic models for request and response schemas.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str