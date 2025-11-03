from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    @validates('email')
    def validate_email(self, key, address):
        """
        Validate the email field to ensure it is not empty and follows the correct format.

        Parameters:
        - key: Name of the field being validated.
        - address: The email address to validate.

        Raises:
        - ValueError: If the email is empty or not in the correct format.
        
        Returns:
        - The validated and cleaned email address.
        """
        if not address:
            raise ValueError("E001: Email address cannot be empty.")
        
        if "@" not in address or "." not in address.split("@")[-1]:
            raise ValueError("E002: Invalid email format.")
        
        return address  # Return the validated email address if no exceptions are raised

    def __repr__(self):
        return f"<Teacher(name={self.name}, email={self.email})>"