from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Represents a Course entity in the database."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Course name is required
    level = Column(String, nullable=False)  # Course level is required

def init_db(engine):
    """Initialize the database by creating tables."""
    
    # Create all tables if they do not exist
    Base.metadata.create_all(bind=engine)  # Ensures courses table is created
    
    # Additional logic for creating a new Course table if it doesn't exist
    inspector = inspect(engine)
    if "courses" not in inspector.get_table_names():  # Check if courses table exists
        with engine.begin() as connection:
            connection.execute('CREATE TABLE courses (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, level TEXT NOT NULL)')