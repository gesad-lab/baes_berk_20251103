# src/models/teacher.py
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    """Define the structure of the Teacher entity."""
    __tablename__ = 'teachers'

    id = Column(String, primary_key=True, index=True)  # Auto-generated ID
    name = Column(String, nullable=False)  # Required teacher name
    email = Column(String, nullable=False, unique=True)  # Required teacher email (must be unique)

    def __repr__(self):
        """Return a string representation of the Teacher entity."""
        return f"<Teacher(id='{self.id}', name='{self.name}', email='{self.email}')>"