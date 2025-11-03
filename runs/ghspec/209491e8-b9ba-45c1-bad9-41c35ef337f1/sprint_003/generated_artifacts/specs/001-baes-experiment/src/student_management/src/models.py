from sqlalchemy import Column, Integer, String
from src.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for each course
    name = Column(String, nullable=False)  # Name of the course, must be provided
    level = Column(String, nullable=False)  # Level of the course, must be provided

    def __repr__(self):
        return f"<Course(name={self.name}, level={self.level})>"