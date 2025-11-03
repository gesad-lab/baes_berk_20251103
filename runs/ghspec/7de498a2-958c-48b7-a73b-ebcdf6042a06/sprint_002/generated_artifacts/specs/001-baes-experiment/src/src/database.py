from sqlalchemy import Column, Integer, String
from src.database import Base

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New field added here with not null constraint

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Student(name={self.name}, email={self.email})>"