'''
Defines the SQLAlchemy model for the Student entity and Pydantic model for input validation.
'''
from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel, EmailStr
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # New email field with validation