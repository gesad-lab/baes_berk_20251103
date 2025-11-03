from sqlalchemy import Column, Integer, String
from database import Base

class Course(Base):
    """
    Course model to represent a course within the educational application.

    Attributes:
    - id (int): Primary key for the course.
    - name (str): The name of the course (required).
    - level (str): The level of the course (required).
    """

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)