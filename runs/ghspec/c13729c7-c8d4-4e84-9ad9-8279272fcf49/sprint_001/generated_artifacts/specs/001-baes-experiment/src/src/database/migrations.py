from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL (SQLite in this case)
DATABASE_URL = "sqlite:///./students.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a base class for declarative models
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

def create_database_schema():
    """Create the database schema if it doesn't exist."""
    try:
        # Create all tables in the database
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        # Log the error and re-raise it for handling elsewhere
        print(f"Error creating database schema: {e}")
        raise

if __name__ == "__main__":
    # Invoke schema creation when this module is executed
    create_database_schema()