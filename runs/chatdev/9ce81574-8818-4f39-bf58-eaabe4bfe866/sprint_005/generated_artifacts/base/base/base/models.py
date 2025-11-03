'''
Defines the SQLAlchemy model for the Student entity.
'''
from sqlalchemy import Column, Integer, String
from database import Base
class Student(Base):
    '''
    SQLAlchemy model for the Student entity.
    Attributes:
    - id: int - The primary key for the student.
    - name: str - The name of the student.
    - email: str - The email of the student.
    '''
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # Add this line