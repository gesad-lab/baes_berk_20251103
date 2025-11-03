from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    """
    Represents a student entity in the database.
    
    Attributes:
    - id (int): Primary key for the student.
    - name (str): The name of the student, must be unique and non-null.
    """
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Name is required field
