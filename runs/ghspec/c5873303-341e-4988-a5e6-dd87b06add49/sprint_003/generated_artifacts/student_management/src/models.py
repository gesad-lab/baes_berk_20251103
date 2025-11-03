from sqlalchemy import Column, Integer, String
from src.database import Base

class Course(Base):
    """Course model representing a course entity in the system."""
    
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field for the course name
    level = Column(String, nullable=False)  # Required field for the course level