from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field
    email = Column(String, nullable=False)  # New required email field, must be in standard format

    def __init__(self, name: str, email: str):
        # Initialize name and email for a new student entity
        self.name = name
        self.email = email

    def validate_email(self) -> bool:
        """
        Validate the email format.
        
        :return: True if the email is valid, False otherwise.
        """
        # Simple email validation logic, can be extended if needed
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, self.email) is not None

    # Optionally, add a __repr__ method for easier debugging
    def __repr__(self):
        return f"<Student(name={self.name}, email={self.email})>"