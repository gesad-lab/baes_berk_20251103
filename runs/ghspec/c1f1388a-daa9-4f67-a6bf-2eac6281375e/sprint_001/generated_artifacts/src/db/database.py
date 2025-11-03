```python
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import OperationalError
import os

# Define the SQLite database URL from environment variables or use a default
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///students.db")

# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a base class for declarative models
Base = declarative_base()

class Student(Base):
    """Student model representing the students table in the database."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

def init_db():
    """Initialize the database and create the necessary tables."""
    try:
        # Create all tables in the database (this will create the students table)
        Base.metadata.create_all(engine)
        print("Database initialized and schema created.")
    except OperationalError as e:
        print(f"Error creating database schema: {e}")

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a scoped session for thread safety
db = scoped_session(SessionLocal)

if __name__ == "__main__":
    init_db()
```