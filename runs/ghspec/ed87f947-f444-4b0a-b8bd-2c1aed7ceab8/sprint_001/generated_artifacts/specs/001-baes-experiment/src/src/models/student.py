from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """
    Represents a student entity in the database.

    Attributes:
        id (int): The unique identifier for the student, auto-generated.
        name (str): The name of the student, which is a required field.
    """
    
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"