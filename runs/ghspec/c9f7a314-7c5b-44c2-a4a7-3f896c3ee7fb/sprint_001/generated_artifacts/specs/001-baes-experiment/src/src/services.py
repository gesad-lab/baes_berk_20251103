```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for SQLAlchemy models
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

# Database connection string
DATABASE_URL = "sqlite:///./students.db"

# Create a SQLAlchemy engine and session maker
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Initializes the database by creating the necessary tables.

    This function creates all tables in the database as defined by the
    SQLAlchemy models. If the tables already exist, this operation will
    not affect them.
    """
    try:
        # Create all tables in the database
        Base.metadata.create_all(bind=engine)
        print("Database initialized successfully.")
    except Exception as e:
        # Log the error and re-raise it for further handling
        print(f"Error initializing the database: {str(e)}")
        raise
```