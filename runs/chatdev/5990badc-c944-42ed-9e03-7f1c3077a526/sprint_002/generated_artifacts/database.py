'''
Database connection and session management.
'''
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def create_database():
    Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def upgrade_database():
    # This function will handle the migration to add the email field
    metadata = MetaData(bind=engine)
    metadata.reflect()
    students_table = metadata.tables['students']
    # Check if the email column already exists
    if 'email' not in students_table.columns:
        with engine.connect() as connection:
            # Create a new table with the email column
            connection.execute('CREATE TABLE students_new (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL)')
            # Copy existing data to the new table
            connection.execute('INSERT INTO students_new (id, name, email) SELECT id, name, "" FROM students')
            # Drop the old table
            connection.execute('DROP TABLE students')
            # Rename the new table to the original table name
            connection.execute('ALTER TABLE students_new RENAME TO students')