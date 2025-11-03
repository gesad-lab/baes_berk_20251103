'''
Pydantic models for data validation and serialization.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str