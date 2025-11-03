```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Course(Base):
    """
    Course Entity representing educational courses in the system.
    
    Attributes:
        id (int): Unique identifier for the course.
        name (str): The name of the course.
        level (str): The difficulty level of the course.
    """
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

# Database engine setup (adapt this based on your configuration)
DATABASE_URL = "sqlite:///./test.db"  # Replace with actual database configuration
engine = create_engine(DATABASE_URL)

# Create all tables, including Course
def create_database():
    Base.metadata.create_all(bind=engine)

# Create a new session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to get a new DB session
def get_db():
    """
    Dependency for getting a database session.
    Yields a database session and ensures it is closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Call this function to create the database 
# Uncomment to create tables if not already created
# create_database()
```