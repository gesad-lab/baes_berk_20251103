'''
Database connection and session management.
'''
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db() -> Session:
    '''
    Create a new database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def init_db() -> None:
    '''
    Initialize the database and create tables.
    '''
    Base.metadata.create_all(bind=engine)
def migrate_db() -> None:
    '''
    Migrate the database to add the email field to the Student entity and create the courses table.
    '''
    metadata = MetaData(bind=engine)
    students_table = Table('students', metadata, autoload_with=engine)
    # Check if the email column already exists
    if 'email' not in students_table.columns:
        with engine.connect() as connection:
            # Add the email column without NOT NULL constraint
            connection.execute(f'ALTER TABLE students ADD COLUMN email TEXT')
            # Optionally, update existing records to set a default value
            connection.execute(f'UPDATE students SET email = "" WHERE email IS NULL')
    # Create the courses table if it doesn't exist
    courses_table = Table('courses', metadata)
    if not courses_table.exists():
        with engine.connect() as connection:
            connection.execute('''
                CREATE TABLE courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    level TEXT NOT NULL
                )
            ''')