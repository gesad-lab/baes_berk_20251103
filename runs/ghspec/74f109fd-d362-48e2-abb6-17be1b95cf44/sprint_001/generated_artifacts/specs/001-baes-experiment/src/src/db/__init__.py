from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Initialize the SQLAlchemy ORM
Base = declarative_base()

# Create an engine for the SQLite database
DATABASE_URL = "sqlite:///./students.db"  # SQLite database located at the project root
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the session
def get_db():
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Provide the session to the caller
    finally:
        db.close()  # Ensure the session is closed after use

# Create all tables in the database (according to the models)
def init_db():
    import src.models  # Import all models to register them with the metadata
    Base.metadata.create_all(bind=engine)  # Create tables in the database based on the models defined

# Call the init_db function to set up the database schema if this file is executed directly
if __name__ == "__main__":
    init_db()  # Initialize the database on script execution