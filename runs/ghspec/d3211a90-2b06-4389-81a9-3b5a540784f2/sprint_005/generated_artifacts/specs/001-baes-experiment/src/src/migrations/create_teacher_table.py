from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

def create_teacher_table():
    """
    Create the teachers table in the database if it does not already exist.
    
    This method initializes the database connection and ensures that the Teacher
    table is created with the specified schema.
    """
    engine = create_engine('sqlite:///database.db')  # Ensure this matches existing database path
    Base.metadata.create_all(engine)  # Create table if it does not exist