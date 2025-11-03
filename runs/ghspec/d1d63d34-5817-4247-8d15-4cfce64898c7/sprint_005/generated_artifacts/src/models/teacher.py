from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    """Model for the Teacher entity in the Student Management Application."""
    
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Teacher's name (required)
    email = Column(String, nullable=False, unique=True)  # Teacher's email (required and unique)

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"