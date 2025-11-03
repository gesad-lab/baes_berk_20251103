from sqlalchemy import Column, Integer, String
from database import Base

class Course(Base):
    """Represents a Course entity in the educational management system."""

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Name of the course
    level = Column(String, nullable=False)  # Level of the course (e.g., Beginner, Intermediate, Advanced)

    def __repr__(self):
        """Return a string representation of the Course instance."""
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"