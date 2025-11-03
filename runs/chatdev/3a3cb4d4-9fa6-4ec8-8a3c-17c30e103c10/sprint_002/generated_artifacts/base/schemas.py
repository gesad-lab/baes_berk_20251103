'''
Defines Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
class StudentResponse(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True