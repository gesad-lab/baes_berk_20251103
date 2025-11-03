from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, exc

Base = declarative_base()

class Student(Base):
    """Student model to represent student records in the database."""
    
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Name is a required field

    def __repr__(self):
        """Return a string representation of the Student instance."""
        return f"<Student(id={self.id}, name='{self.name}')>"

def init_db(database_url: str):
    """Initialize the database and create tables if they do not exist."""
    try:
        engine = create_engine(database_url)
        Base.metadata.create_all(engine)  # Create tables
    except exc.SQLAlchemyError as e:
        # Log the error context (consider using a logging framework in production)
        print(f"Error initializing database: {e}")