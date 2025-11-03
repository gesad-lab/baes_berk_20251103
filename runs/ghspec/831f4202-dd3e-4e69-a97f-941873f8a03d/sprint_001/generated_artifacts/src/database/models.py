from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Student(Base):
    """Student model representing a student record in the database."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each student
    name = Column(String, nullable=False)  # Name of the student, cannot be null

    def __repr__(self):
        """
        Representation of the Student model instance.
        
        Returns:
            str: A string representation of the Student instance.
        """
        return f"<Student(id={self.id}, name='{self.name}')>"

# Database setup
DATABASE_URL = "sqlite:///./students.db"  # SQLite database URL
engine = create_engine(DATABASE_URL)

# Create database tables
Base.metadata.create_all(bind=engine)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Dependency for database session management.
    
    Yields:
        Session: A new SQLAlchemy session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # Ensure the session is closed properly after use
