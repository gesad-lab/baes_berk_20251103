from sqlalchemy import Column, Integer, String
from database import Base  # Assuming a file named database.py for SQLAlchemy setup

class Student(Base):
    """Model representing a student in the system."""
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        """Provide a string representation of the student object."""
        return f"<Student(id={self.id}, name='{self.name}')>"