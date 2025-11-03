'''
Handles the database connection and session management.
'''
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from models import Student, Course, Teacher  # Added imports for necessary classes
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def create_database():
    Base.metadata.create_all(bind=engine)
    # Create the Course table
    Course.__table__.create(bind=engine, checkfirst=True)
    # Create the Teacher table
    Teacher.__table__.create(bind=engine, checkfirst=True)
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def migrate_database():
    # Migration logic for students table
    metadata = MetaData(bind=engine)
    students_table = Table('students', metadata, autoload_with=engine)
    if 'email' not in students_table.columns:
        with engine.connect() as conn:
            # Create a new table with the email column
            conn.execute('''
                CREATE TABLE students_new (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')
            # Copy existing records to the new table
            conn.execute('''
                INSERT INTO students_new (id, name, email)
                SELECT id, name, '' FROM students
            ''')
            # Drop the old table
            conn.execute('DROP TABLE students')
            # Rename the new table to the original table name
            conn.execute('ALTER TABLE students_new RENAME TO students')
    # Add teacher_id to existing courses table if it doesn't exist
    with engine.connect() as conn:
        if 'teacher_id' not in [column[1] for column in conn.execute("PRAGMA table_info(courses)").fetchall()]:
            conn.execute('ALTER TABLE courses ADD COLUMN teacher_id INTEGER')
    # Create the Teacher table if it does not exist
    with engine.connect() as conn:
        if not conn.dialect.has_table(conn, 'teachers'):
            conn.execute('''
                CREATE TABLE teachers (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')
        else:
            # If the table exists, you might want to handle existing data
            print("Teachers table already exists. No changes made.")