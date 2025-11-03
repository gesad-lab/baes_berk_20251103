from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Represents a student in the database.

    Attributes:
        id (int): The unique identifier for the student.
        name (str): The name of the student; must not be null.
    """
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        """Return a string representation of the Student instance.

        Returns:
            str: A string representation of the Student with its id and name.
        """
        return f"<Student(id={self.id}, name='{self.name}'>"