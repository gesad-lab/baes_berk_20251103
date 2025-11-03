'''
Defines the SQLAlchemy models for the application, including Student and Course entities.
'''
from sqlalchemy import Column, Integer, String
from database import Base
class Student(Base):
    '''
    Model for the Student entity.
    '''
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
class Course(Base):
    '''
    Model for the Course entity.
    '''
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)