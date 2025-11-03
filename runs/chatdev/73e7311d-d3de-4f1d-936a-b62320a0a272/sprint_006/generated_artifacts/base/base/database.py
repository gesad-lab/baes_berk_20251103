'''
Database connection and session management.
'''
from sqlalchemy import create_engine, Column, Integer, String, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
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
        # Check and create tables if they don't exist
        if not inspector.has_table("students"):
            Base.metadata.create_all(bind=engine)
        if not inspector.has_table("courses"):
            Base.metadata.create_all(bind=engine)
        if not inspector.has_table("student_courses"):
            Base.metadata.create_all(bind=engine)  # Ensure association table is created
        # Migration logic for adding email column
        if 'email' not in [column['name'] for column in inspector.get_columns('students')]:
            # Step 1: Add email column without NOT NULL constraint
            conn.execute('ALTER TABLE students ADD COLUMN email TEXT')
            # Step 2: Update existing records to set a default value
            conn.execute('UPDATE students SET email = "" WHERE email IS NULL')
            # Step 3: Alter the column to add NOT NULL constraint
            conn.execute('ALTER TABLE students RENAME TO students_old')
            Base.metadata.create_all(bind=engine)  # Recreate the table with the new schema
            conn.execute('INSERT INTO students (id, name, email) SELECT id, name, email FROM students_old')
            conn.execute('DROP TABLE students_old')