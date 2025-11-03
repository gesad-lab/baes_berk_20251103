from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)  # Unique ID for each student
    name = Column(String, index=True, nullable=False)     # Name of the student (required field)