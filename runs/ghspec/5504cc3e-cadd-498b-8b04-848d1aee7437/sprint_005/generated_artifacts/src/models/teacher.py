from sqlalchemy import Column, Integer, String
from your_application import db

class Teacher(db.Model):
    """Model representing a teacher in the system."""
    
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Name of the teacher
    email = Column(String, nullable=False, unique=True)  # Unique email for the teacher

    def __repr__(self):
        """Return a string representation of the Teacher model."""
        return f"<Teacher(id={self.id}, name='{self.name}', email='{self.email}')>"