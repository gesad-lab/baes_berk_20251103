'''
Defines the SQLAlchemy models for the Student and Course entities.
'''
from sqlalchemy import Column, Integer, String
from database import Base
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String)  # Added email field, initially allowing NULL
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Course name is required
    level = Column(String, nullable=False)  # Course level is required