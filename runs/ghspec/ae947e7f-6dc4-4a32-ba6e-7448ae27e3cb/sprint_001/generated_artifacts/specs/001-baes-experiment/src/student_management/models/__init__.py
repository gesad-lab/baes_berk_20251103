from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize the SQLAlchemy Base
Base = declarative_base()

# Database configuration
DATABASE_URL = "sqlite:///./students.db"

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Create the database schema on startup."""
    Base.metadata.create_all(bind=engine)