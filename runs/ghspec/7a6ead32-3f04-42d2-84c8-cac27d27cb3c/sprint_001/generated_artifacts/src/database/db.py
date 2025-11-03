from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for our models
Base = declarative_base()

class Student(Base):
    """Student model representing a record in the students table."""
    
    __tablename__ = 'students'  # Define the table name in the database
    
    # Define the columns for the Student entity
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier
    name = Column(String, nullable=False)  # Student's name, cannot be null

    def __repr__(self):
        """Return a string representation of the Student instance."""
        return f"<Student(id={self.id}, name={self.name})>"