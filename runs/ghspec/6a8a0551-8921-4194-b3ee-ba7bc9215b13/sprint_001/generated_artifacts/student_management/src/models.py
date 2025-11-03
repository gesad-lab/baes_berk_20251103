```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy database setup
DATABASE_URL = "sqlite:///students.db"  # SQLite database file
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

# Create a new database session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def initialize_database():
    """Check for the existence of the students table and create it if necessary."""
    # Create the database and tables if they don't exist
    try:
        Base.metadata.create_all(engine)  # Create all tables in the base
        print("Database initialized and student table created if it did not exist.")
    except Exception as e:
        # Log the error with context for debugging
        print(f"Error initializing the database: {e}")

# Call the function to initialize the database on startup
initialize_database()
```