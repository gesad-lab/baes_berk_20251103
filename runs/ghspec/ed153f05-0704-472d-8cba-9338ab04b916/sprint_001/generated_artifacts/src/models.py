from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Student(Base):
    """Defines the Student model for database access."""

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name})>"

# Database setup (to be expanded in database.py)
DATABASE_URL = "sqlite:///students.db"  # Example SQLite URL
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  # Create tables in the database

# Session factory for interacting with the database
Session = sessionmaker(bind=engine)