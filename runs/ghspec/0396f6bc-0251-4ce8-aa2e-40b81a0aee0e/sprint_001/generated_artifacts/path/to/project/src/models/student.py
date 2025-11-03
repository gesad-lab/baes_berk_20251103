from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class Student(Base):
    """
    Represents a student entity in the database.

    Attributes:
        id (int): The unique identifier for the student.
        name (str): The name of the student.
    """
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    @validates('name')
    def validate_name(self, key, name):
        """
        Validates the student's name for length and format.

        Args:
            key (str): The key being validated.
            name (str): The name to validate.

        Returns:
            str: The validated name.

        Raises:
            ValueError: If the name is empty or exceeds the maximum length.
        """
        if not name:
            raise ValueError("Name is required")
        if len(name) > 100:  # Assuming max length for names is 100 characters
            raise ValueError("Name must not exceed 100 characters")
        return name