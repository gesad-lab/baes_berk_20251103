from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)  # New email field added.

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Validate email format using Pydantic

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True  # Enable compatibility with ORM instances

# Additional methods and logic for handling Student instances can be added as needed.