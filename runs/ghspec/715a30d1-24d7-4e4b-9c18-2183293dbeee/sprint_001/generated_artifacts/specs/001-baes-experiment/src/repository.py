```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Define the base for SQLAlchemy models
Base = declarative_base()

# Database URL for SQLite
DATABASE_URL = "sqlite:///./test.db"  # Change to your preferred database URL

# Create an engine to connect to the database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Student model representing the 'students' table
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

def init_db():
    """Create the database schema on startup."""
    # Create the tables in the database
    Base.metadata.create_all(bind=engine)

def get_db():
    """Get a new database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Automatically create the database schema when the application starts
init_db()
```