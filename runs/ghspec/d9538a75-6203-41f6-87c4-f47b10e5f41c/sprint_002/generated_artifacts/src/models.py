from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import re

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate the format of the email address.

        Parameters:
        - email (str): The email address to validate.

        Returns:
        - bool: True if the email is valid, False otherwise.
        """
        if not email:
            return False
        # Simple regex for basic email validation
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None

    def as_dict(self):
        """
        Convert Student instance into a dictionary.

        Returns:
        - dict: Dictionary representation of the student instance.
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }