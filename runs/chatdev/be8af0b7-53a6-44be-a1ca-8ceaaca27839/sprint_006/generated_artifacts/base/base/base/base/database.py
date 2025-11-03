'''
Handles database connection and session management.
'''
from sqlalchemy import create_engine, Column, String, text  # Import text for SQL execution
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def create_database():
    '''
    Creates the database and tables if they do not exist.
    '''
    Base.metadata.create_all(bind=engine)
def migrate_database():
    '''
    Migrates the database to add the email field to the Student entity.
    '''
    with engine.connect() as connection:
        # Check if the 'email' column already exists
        result = connection.execute(text("PRAGMA table_info(students)"))
        columns = [row[1] for row in result]
        if 'email' not in columns:
            connection.execute(text('ALTER TABLE students ADD COLUMN email VARCHAR'))
def get_db() -> Session:
    '''
    Dependency that provides a database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()