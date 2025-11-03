from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Create the SQLAlchemy engine to connect to the SQLite database
engine = create_engine('sqlite:///students.db')

# Create a base class for declarative models
Base = declarative_base()

# Create a session maker for database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Dependency that provides a database session for route handlers."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()