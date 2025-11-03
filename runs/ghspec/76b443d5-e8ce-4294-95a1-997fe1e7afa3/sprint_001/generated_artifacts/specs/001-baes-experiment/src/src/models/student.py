from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    """Database model for the Student entity."""
    
    __tablename__ = "students"

    # An auto-incrementing identifier for the Student
    id = Column(Integer, primary_key=True, index=True)

    # The name of the Student, which is a required field
    name = Column(String, nullable=False)  # Cannot be null or empty

    def __repr__(self):
        """Return a string representation of the Student object."""
        return f"<Student(id={self.id}, name={self.name})>"