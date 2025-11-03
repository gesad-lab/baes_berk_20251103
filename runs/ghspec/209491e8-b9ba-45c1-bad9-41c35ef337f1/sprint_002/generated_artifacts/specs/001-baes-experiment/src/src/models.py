from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import re

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  # New email attribute, required and must be unique

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate the email format."""
        email_regex = r'^[\w\.-]+@\w+\.\w+$'  # Simple regex for email validation
        return re.match(email_regex, email) is not None
        
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"