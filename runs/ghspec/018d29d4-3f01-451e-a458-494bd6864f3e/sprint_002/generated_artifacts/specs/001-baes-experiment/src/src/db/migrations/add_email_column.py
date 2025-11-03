import re
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    @classmethod
    def validate_email(cls, email: str) -> bool:
        """
        Validates the email format using a regular expression.
        
        Args:
            email (str): The email address to validate.
        
        Returns:
            bool: True if the email is valid, False otherwise.
        """
        # Regular expression for validating an Email
        regex = r"[^@]+@[^@]+\.[^@]+"
        
        return re.match(regex, email) is not None

    @classmethod
    def create_student(cls, session, name: str, email: str):
        """
        Creates a new student in the database after validating name and email.
        
        Args:
            session: The SQLAlchemy session to use for database operations.
            name (str): The student's name.
            email (str): The student's email address.

        Raises:
            ValueError: If name is empty or email is invalid.
            IntegrityError: If there is a database error during insertion.
        """
        if not name:
            raise ValueError("Name is required")
        
        if not cls.validate_email(email):
            raise ValueError("Invalid email format")

        student = cls(name=name, email=email)
        session.add(student)

        try:
            session.commit()  # Attempts to save the new student
        except IntegrityError:
            session.rollback()
            raise IntegrityError("Error saving the student in the database. Ensure student data is unique.")

# Related migration logic would need to be added for the email column in the actual migration file.