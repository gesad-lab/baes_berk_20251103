```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# This base class will be subclassed by the Course model
Base = declarative_base()

# Set up the SQLite database engine
DATABASE_URL = "sqlite:///./test.db"  # Replace with your actual database URL
engine = create_engine(DATABASE_URL)

# Define the Course model
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Course name is required
    level = Column(String, nullable=False)  # Course level is required

# Initialize the database
def create_schema():
    """Create the database schema."""
    # Creating all tables (including the new Course table)
    Base.metadata.create_all(bind=engine)

# SQLAlchemy session management
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Create a new database session for each request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```