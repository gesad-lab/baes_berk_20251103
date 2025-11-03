```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import re

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    @classmethod
    def validate_email(cls, email: str) -> bool:
        """Validates the email format.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email is in a valid format, False otherwise.
        """
        # Regular expression for validating an Email
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    @staticmethod
    def create_student(name: str, email: str):
        """Creates a new student after validating the email.

        Args:
            name (str): The name of the student.
            email (str): The email address of the student.

        Raises:
            ValueError: If the email is not valid.
        """
        if not Student.validate_email(email):
            raise ValueError("Invalid email format.")
        # Assuming we have access to the session here to add the student
        new_student = Student(name=name, email=email)
        return new_student
```