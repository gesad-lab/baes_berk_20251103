'''
Handles database connections and session management.
'''
from sqlalchemy import create_engine, MetaData, Table
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
    Base.metadata.create_all(bind=engine)  # Create tables first
    migrate_database()  # Then perform migration
def migrate_database():
    '''
    Migrates the database to add the email column to the Student table.
    '''
    metadata = MetaData(bind=engine)
    if 'students' in metadata.tables:
        students_table = Table('students', metadata, autoload_with=engine)
        # Check if the email column already exists
        if 'email' not in students_table.columns:
            with engine.connect() as connection:
                connection.execute('ALTER TABLE students ADD COLUMN email STRING NOT NULL')
    else:
        # If the table does not exist, you may want to create it or handle it accordingly
        print("The 'students' table does not exist.")
def get_db() -> Session:
    '''
    Provides a database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()