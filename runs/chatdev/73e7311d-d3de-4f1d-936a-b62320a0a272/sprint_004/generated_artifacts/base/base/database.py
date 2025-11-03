'''
Database connection and session management.
'''
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import inspect
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Function to create the database schema
def init_db():
    # Create a connection to the database
    with engine.connect() as conn:
        inspector = inspect(conn)
        if not inspector.has_table("students"):
            Base.metadata.create_all(bind=engine)
        else:
            # Logic to add email column without losing data
            if 'email' not in [column['name'] for column in inspector.get_columns('students')]:
                # Step 1: Add the email column without NOT NULL constraint
                conn.execute('ALTER TABLE students ADD COLUMN email TEXT')
                # Step 2: Update existing records to set a default value
                conn.execute('UPDATE students SET email = "" WHERE email IS NULL')
                # Step 3: Alter the column to add NOT NULL constraint
                conn.execute('ALTER TABLE students RENAME TO students_old')
                Base.metadata.create_all(bind=engine)  # Recreate the table with the new schema
                conn.execute('INSERT INTO students (id, name, email) SELECT id, name, email FROM students_old')
                conn.execute('DROP TABLE students_old')