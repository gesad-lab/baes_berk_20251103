from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """
    Course model to define the database schema for courses.
    Attributes:
        id (int): Primary key for the Course entity.
        name (str): The name of the course (required).
        level (str): The level of the course (required).
    """

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)  # Primary key for each course
    name = Column(String, nullable=False)  # Course name, must be provided
    level = Column(String, nullable=False)  # Course level, must be provided

    def __repr__(self):
        return f"<Course(name={self.name}, level={self.level})>"