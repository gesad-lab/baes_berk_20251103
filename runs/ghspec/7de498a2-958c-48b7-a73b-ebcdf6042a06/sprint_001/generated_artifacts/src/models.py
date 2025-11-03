from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative models
Base = declarative_base()

class Student(Base):
    """Database model for a student."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        """Return a string representation of the Student object."""
        return f"<Student(id={self.id}, name={self.name})>"