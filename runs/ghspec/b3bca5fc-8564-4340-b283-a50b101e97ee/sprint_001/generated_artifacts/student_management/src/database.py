from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# Create a SQLAlchemy engine for SQLite
DATABASE_URL = "sqlite:///./students.db"  # Relative path to SQLite database file
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a base class for declarative models
Base = declarative_base()

# Create a session class and a scoped session
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def init_db():
    """Initialize the database by creating the tables."""
    # Import models here to ensure they are registered with the Base
    from models import Student  # noqa: F401
    Base.metadata.create_all(bind=engine)

def get_db():
    """Yield a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # Ensure the session is closed after use