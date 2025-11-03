# app/models/student.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field added

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate the email format.
        
        Args:
            email (str): The email address to validate.
            
        Returns:
            bool: True if valid format, False otherwise.
        """
        import re
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None

# Rest of the existing model logic remains unchanged...