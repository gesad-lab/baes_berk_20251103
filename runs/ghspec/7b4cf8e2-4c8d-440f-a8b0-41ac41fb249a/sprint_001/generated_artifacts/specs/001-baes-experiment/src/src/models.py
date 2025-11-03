from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///students.db"  # SQLite database URL

# Create an engine
engine = create_engine(DATABASE_URL)

# Define a base class for declarative models
Base = declarative_base()

class Student(Base):
    """Model representing a student."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Name is mandatory

def initialize_database():
    """Create the database and the necessary tables."""
    Base.metadata.create_all(bind=engine)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Dependency for database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize the database at application startup
if __name__ == "__main__":
    initialize_database()  # This will create the database and tables if they do not exist