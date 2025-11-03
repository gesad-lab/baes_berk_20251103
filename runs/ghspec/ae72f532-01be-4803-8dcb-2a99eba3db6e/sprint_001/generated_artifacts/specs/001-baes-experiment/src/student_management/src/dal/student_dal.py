```python
# student_management/src/models/student.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class Student(Base):
    """
    Represents a student entity in the database.

    Attributes:
        id (int): The unique identifier for the student.
        name (str): The name of the student, required for student creation.
    """
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Name is a mandatory field

    @validates('name')
    def validate_name(self, key, name):
        """
        Validates the 'name' attribute to ensure it is not empty.

        Args:
            key (str): The attribute name.
            name (str): The name being validated.

        Raises:
            ValueError: If the name is empty or contains only whitespace.
        """
        if not name or name.strip() == "":
            raise ValueError("Name is required and cannot be empty.")
        return name
```