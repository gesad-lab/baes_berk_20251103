from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Define the SQLAlchemy Base for model definitions
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

# Database setup and schema creation
DATABASE_URL = "sqlite:///./students.db"

# Create engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Create the database schema."""
    # Create all tables in the database which are defined by Base's subclasses
    Base.metadata.create_all(bind=engine)
  
# No code should be executed at import time; functions can be imported elsewhere to integrate  
if __name__ == "__main__":
    init_db()  # Automatically initialize database schema when running this module.