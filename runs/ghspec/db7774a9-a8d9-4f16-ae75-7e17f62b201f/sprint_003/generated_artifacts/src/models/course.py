from sqlalchemy import Column, Integer, String
from src.database import Base

class Course(Base):
    """Course model representing the database table for courses."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    level = Column(String, index=True, nullable=False)
    
    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}')>"
    
    @staticmethod
    def validate_course_data(name: str, level: str) -> None:
        """Validate course input data for creating a new course.
        
        Args:
            name (str): The name of the course.
            level (str): The level of the course.
        
        Raises:
            ValueError: If the name or level is missing or empty.
        """
        if not name or not level:
            raise ValueError("Both 'name' and 'level' are required fields.")