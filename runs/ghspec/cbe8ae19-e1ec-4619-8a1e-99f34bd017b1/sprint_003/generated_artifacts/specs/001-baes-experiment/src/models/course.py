from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()

class Course(Base):
    """
    Represents a course entity in the database.

    Attributes:
        id (int): The unique identifier for the course (Primary Key).
        name (str): The name of the course (Required).
        level (str): The educational level of the course (Required).
    """
    
    __tablename__ = 'courses'  # Define the table name

    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-incrementing primary key
    name = Column(String, nullable=False)  # Course name must be a valid string
    level = Column(String, nullable=False)  # Course level must be a valid string

    def __repr__(self):
        """Provide a string representation of the Course instance."""
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}')>"