from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class StudentCreate(BaseModel):
    name: str

    class Config:
        # This config is used to allow the model to parse data nested under a different key
        orm_mode = True