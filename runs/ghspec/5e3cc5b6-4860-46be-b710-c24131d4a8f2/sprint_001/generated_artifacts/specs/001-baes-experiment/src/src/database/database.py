from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL for SQLite, you can replace 'sqlite:///./test.db' with your own database URL
DATABASE_URL = "sqlite:///./test.db"

# Create an SQLAlchemy engine instance
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a declarative base class
Base = declarative_base()

# Create a session local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Dependency that provides a database session to the FastAPI path operations.
    
    Yields:
        Session: A database session instance to be used for transactions.
    """
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()  # Ensure the session is closed after use

# Create the database tables if they don't exist yet
def init_db():
    """
    Initializes the database by creating all tables defined by the ORM models.
    This function should be called at startup.
    """
    Base.metadata.create_all(bind=engine)  # Create tables based on the Base metadata

# Initialize the database table on first run.
init_db()  # Uncomment this line to create tables on startup.