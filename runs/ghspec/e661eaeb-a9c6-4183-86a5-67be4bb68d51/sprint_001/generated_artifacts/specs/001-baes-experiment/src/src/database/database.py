from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for the declarative model
Base = declarative_base()

# Database URL for SQLite
DATABASE_URL = "sqlite:///./students.db"

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create all tables in the database
def init_db():
    """Create the database schema on application startup."""
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        # Log the error with a message
        print(f"Error while creating the database schema: {str(e)}")

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# A function to get a new session (can be used in application when needed)
def get_db():
    """Create a new database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize the database schema when this module is imported
init_db()