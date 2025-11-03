'''
Defines the SQLAlchemy model for the Student entity and Pydantic model for input validation.
'''
from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
class StudentCreate(BaseModel):
    name: str