from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import re

Base = declarative_base()

class Student(Base):  # Assuming Base is defined elsewhere as part of the SQLAlchemy setup
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validates the email format.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email format is valid, False otherwise.
        """
        if not email:
            return False
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    @classmethod
    def create_student(cls, name: str, email: str):
        """Creates a new student instance after validating the input.

        Args:
            name (str): The name of the student.
            email (str): The email of the student.

        Raises:
            ValueError: If the email is invalid or name is empty.

        Returns:
            Student: A new student instance.
        """
        if not cls.validate_email(email):
            raise ValueError(f"Invalid email format: {email}")
        if not name:
            raise ValueError("Name cannot be empty.")
        
        return cls(name=name, email=email)