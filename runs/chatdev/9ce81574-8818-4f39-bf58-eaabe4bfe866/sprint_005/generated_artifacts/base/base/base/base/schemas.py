'''
Defines the Pydantic models for request validation and response serialization.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str