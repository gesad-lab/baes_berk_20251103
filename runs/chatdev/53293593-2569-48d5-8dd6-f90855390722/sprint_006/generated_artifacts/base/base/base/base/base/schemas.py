'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
class StudentSchema(BaseModel):
    name: str
    class Config:
        orm_mode = True