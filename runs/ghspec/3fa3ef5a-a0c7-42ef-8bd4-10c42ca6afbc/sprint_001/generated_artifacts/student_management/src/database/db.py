```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """
    Represents a Student entity in the database.

    Attributes:
        id (int): The unique identifier for the Student.
        name (str): The name of the Student, must be a non-empty string.
    """

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name})>"

    def to_dict(self):
        """
        Convert the Student instance to a dictionary representation.

        Returns:
            dict: A dictionary containing the Student's id and name.
        """
        return {
            "id": self.id,
            "name": self.name
        }
```