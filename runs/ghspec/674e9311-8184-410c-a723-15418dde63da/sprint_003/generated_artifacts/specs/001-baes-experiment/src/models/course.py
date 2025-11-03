from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define a base class for declarative models
Base = declarative_base()

class Course(Base):
    """Course model representing a course in the system."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    def __init__(self, name: str, level: str):
        """Initialize a new Course instance.

        Parameters:
        - name (str): The name of the course.
        - level (str): The level of the course.
        """
        self.name = name
        self.level = level

    def __repr__(self):
        """Return a string representation of the Course instance."""
        return f"<Course(name='{self.name}', level='{self.level}'>"