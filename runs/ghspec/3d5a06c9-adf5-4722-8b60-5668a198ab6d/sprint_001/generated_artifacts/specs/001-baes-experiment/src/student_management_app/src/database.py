from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Declaring the base model for SQLAlchemy
Base = declarative_base()

# Defining the Student model
class Student(Base):
    __tablename__ = 'students'  # Table name in the database
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique ID for each student
    name = Column(String, nullable=False)  # Student's name, cannot be null

def init_db():
    """
    Initializes the SQLite database and creates the necessary schema.
    This function will be called during application startup.
    """
    # Create a new SQLite database (or connect to the existing one)
    engine = create_engine('sqlite:///students.db')

    # Create all tables in the database (including students table)
    Base.metadata.create_all(engine)

# Function to get a new session to interact with the database
def get_db_session():
    """
    Creates a new database session and returns it.
    This function can be used in the API route handlers for database operations.
    """
    Session = sessionmaker(bind=create_engine('sqlite:///students.db'))
    return Session()  # Return a new session instance