from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Define the base class for declarative models
Base = declarative_base()

class Student(Base):
    """
    Student model representing a student in the database.

    Attributes:
        id (int): Unique identifier for the student.
        name (str): Name of the student. Must be provided and cannot be empty.
    """
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name})>"

# Create SQLite database engine
engine = create_engine('sqlite:///students.db')

# Create all tables in the database (this creates the students table)
Base.metadata.create_all(engine)

# Setup session
Session = sessionmaker(bind=engine)
session = Session()