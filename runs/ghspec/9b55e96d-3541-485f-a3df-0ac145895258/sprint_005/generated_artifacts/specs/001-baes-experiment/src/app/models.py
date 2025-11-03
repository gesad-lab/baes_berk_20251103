from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    """
    Teacher model representing a teacher entity in the application.
    
    Attributes:
        id (int): Primary key, auto-incremental identifier for each teacher.
        name (str): Name of the teacher, cannot be null.
        email (str): Email of the teacher, must be unique and cannot be null.
    """
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
    __table_args__ = (UniqueConstraint('email', name='_email_uc'),)  # Ensures email uniqueness