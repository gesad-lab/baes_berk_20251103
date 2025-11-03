import os
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base for the models
Base = declarative_base()

# Define the Course model
class Course(Base):
    __tablename__ = 'courses'

    # Define the columns for the courses table
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

def create_courses_table():
    """Function to create the courses table in the database."""
    # Database URL can be set here, for example using an environment variable
    database_url = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    
    # Create a database connection
    engine = create_engine(database_url)

    # Create the courses table if it doesn't exist
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_courses_table()