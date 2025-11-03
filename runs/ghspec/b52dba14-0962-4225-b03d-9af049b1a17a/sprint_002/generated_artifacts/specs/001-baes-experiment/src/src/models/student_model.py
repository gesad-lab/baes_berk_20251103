from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import re  # Regex for email validation

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  # New email field, unique for each student

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate the provided email address format.
        
        Args:
            email (str): The email address to validate.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        # Regex pattern for validating an Email
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_pattern, email) is not None

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"