from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    """Model for the Teacher entity, representing an educator in the system."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Name of the teacher, required
    email = Column(String, unique=True, nullable=False)  # Unique email for the teacher, required
    
    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}', email='{self.email}')>"