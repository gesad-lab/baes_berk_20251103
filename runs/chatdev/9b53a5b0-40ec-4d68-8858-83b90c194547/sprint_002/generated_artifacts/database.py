'''
Handles the database connection and session management.
'''
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def create_database():
    Base.metadata.create_all(bind=engine)
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def migrate_database():
    # Migration logic to add the email column to the existing students table
    metadata = MetaData(bind=engine)
    students_table = Table('students', metadata, autoload_with=engine)
    if 'email' not in students_table.columns:
        with engine.connect() as conn:
            # Step 1: Create a new table with the email column
            conn.execute('''
                CREATE TABLE students_new (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')
            # Step 2: Copy existing records to the new table
            conn.execute('''
                INSERT INTO students_new (id, name, email)
                SELECT id, name, '' FROM students
            ''')
            # Step 3: Drop the old table
            conn.execute('DROP TABLE students')
            # Step 4: Rename the new table to the original table name
            conn.execute('ALTER TABLE students_new RENAME TO students')