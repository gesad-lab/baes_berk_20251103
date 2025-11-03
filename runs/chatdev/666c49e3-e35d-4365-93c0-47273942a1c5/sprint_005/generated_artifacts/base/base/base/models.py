'''
Defines the SQLAlchemy model for the Student entity and the Pydantic model for request validation.
'''
from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # Add email field
class StudentCreate(BaseModel):
    name: str
    email: str  # Add email field