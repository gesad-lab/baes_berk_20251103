from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Course model representing a course in the academic system."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each course
    name = Column(String, nullable=False)  # Name of the course, must not be null
    level = Column(String, nullable=False)  # Level of the course, must not be null

def initialize_database(db_url: str):
    """Initialize the database connection and create the necessary tables."""
    
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)  # Create all tables, including the new courses table based on the model structure.