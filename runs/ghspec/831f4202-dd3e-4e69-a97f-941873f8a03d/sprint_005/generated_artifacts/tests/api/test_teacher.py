```python
# src/database.py

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a base class for the SQLAlchemy models
Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Primary key
    name = Column(String, nullable=False)  # Teacher's name (required)
    email = Column(String, unique=True, nullable=False)  # Teacher's email (required, must be unique)

# Database setup
DATABASE_URL = "sqlite:///./test.db"  # Change to your actual database URL

# Creating the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database and create tables."""
    # Create all tables in the database, including the Teacher table
    Base.metadata.create_all(bind=engine)

# Function to get session
def get_db():
    """Generator that provides database session."""
    db = SessionLocal()
    try:
        yield db  # This allows dependency injection of the session in FastAPI routes
    finally:
        db.close()  # Ensure the session is closed after use

# Ensure existing student and course tables are intact while adding the Teacher table
```
