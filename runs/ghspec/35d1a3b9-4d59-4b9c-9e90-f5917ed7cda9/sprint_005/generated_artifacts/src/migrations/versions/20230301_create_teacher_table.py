from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define the base class for SQLAlchemy models
Base = declarative_base()

class Teacher(Base):
    """Represents a teacher in the system."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field for teacher's name
    email = Column(String, unique=True, nullable=False)  # Required unique field for teacher's email