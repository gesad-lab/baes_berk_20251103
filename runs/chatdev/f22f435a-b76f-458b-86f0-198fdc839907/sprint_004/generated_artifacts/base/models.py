'''
Defines the SQLAlchemy models for the application.
'''
from sqlalchemy import Column, Integer, String
from database import Base
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # Added email field
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Required field
    level = Column(String, nullable=False)  # Required field