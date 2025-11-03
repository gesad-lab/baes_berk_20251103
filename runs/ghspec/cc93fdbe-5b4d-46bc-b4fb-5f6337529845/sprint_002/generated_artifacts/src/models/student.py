from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Model representing a student in the database."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
    __table_args__ = (UniqueConstraint('email', name='uq_email'),)  # Ensure email is unique

    def __repr__(self):
        """String representation of the Student model."""
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"