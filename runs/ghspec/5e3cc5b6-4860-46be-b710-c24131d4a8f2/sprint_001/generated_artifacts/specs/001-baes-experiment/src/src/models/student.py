from sqlalchemy import Column, Integer, String
from database.database import Base

class Student(Base):
    """SQLAlchemy model for the Student entity."""
    
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Student name, required field

    def __repr__(self):
        """Return a string representation of the Student object."""
        return f"<Student(id={self.id}, name={self.name})>"