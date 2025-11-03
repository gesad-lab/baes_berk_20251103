from extensions import db  # Assuming you use SQLAlchemy for database interaction
from sqlalchemy import Column, Integer, String

class Teacher(db.Model):
    """Teacher model to represent a teacher entity in the system."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the teacher
    name = Column(String(100), nullable=False)  # Name of the teacher
    email = Column(String(100), nullable=False, unique=True)  # Email of the teacher
