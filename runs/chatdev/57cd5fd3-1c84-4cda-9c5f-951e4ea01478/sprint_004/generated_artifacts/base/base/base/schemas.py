'''
Pydantic models for request and response validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str