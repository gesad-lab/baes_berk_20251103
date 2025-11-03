from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Define the base model for SQLAlchemy
Base = declarative_base()

class Student(Base):
    """Represent the Student entity in the database."""
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for each student
    name = Column(String, nullable=False)  # Student's name - required field

def create_database():
    """Create the SQLite database and the Student table if it doesn't exist."""
    try:
        # Define the SQLite database URL
        engine = create_engine("sqlite:///./students.db")
        
        # Create the tables in the database
        Base.metadata.create_all(bind=engine)
        print("Database and tables created successfully.")
    except SQLAlchemyError as e:
        # Logging error context for debugging
        print(f"Error occurred while creating the database: {e}")

# Create the database upon startup
if __name__ == "__main__":
    create_database()