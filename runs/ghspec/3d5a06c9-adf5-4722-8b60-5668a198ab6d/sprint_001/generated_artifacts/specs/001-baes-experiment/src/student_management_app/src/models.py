from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for declarative table definitions
Base = declarative_base()

# Define the Student model for the students table
class Student(Base):
    __tablename__ = 'students'
    
    # Primary key for the student record
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Name of the student, must be a non-null string
    name = Column(String, nullable=False)

def init_db():
    """
    Initializes the database and creates the schema.
    
    Connects to the SQLite database and creates the students table
    based on the defined models. This function should be called during
    application startup to ensure that the database schema is ready for use.
    """
    try:
        # Create an SQLite database engine
        engine = create_engine('sqlite:///students.db')

        # Create all tables in the database that are defined by the Base subclasses
        Base.metadata.create_all(engine)
        print("Database and tables created successfully.")
    except Exception as e:
        # Log any errors that occur during the database initialization
        print(f"Error initializing the database: {e}")
        raise