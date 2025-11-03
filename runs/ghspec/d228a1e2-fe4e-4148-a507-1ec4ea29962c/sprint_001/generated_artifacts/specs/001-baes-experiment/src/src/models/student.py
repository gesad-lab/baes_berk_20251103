from sqlalchemy import Column, Integer, String
from app import db

class Student(db.Model):
    """
    Represents a student entity in the system.

    Attributes:
        id (int): Unique identifier for the student.
        name (str): Name of the student (mandatory field).
    """
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __init__(self, name: str):
        """
        Initializes a new instance of the Student class.

        Parameters:
            name (str): Name of the student.
        """
        self.name = name

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name})>"