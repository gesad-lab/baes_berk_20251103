from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    """Represents a student entity in the database."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        """Return a string representation of the Student object."""
        return f"<Student(id={self.id}, name='{self.name}')>"