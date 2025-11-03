from app import db
from sqlalchemy import Column, Integer, String

class Teacher(db.Model):
    """Represents a teacher in the system."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the teacher
    name = Column(String, nullable=False)  # The name of the teacher
    email = Column(String, nullable=False)  # The email of the teacher, must be unique

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"