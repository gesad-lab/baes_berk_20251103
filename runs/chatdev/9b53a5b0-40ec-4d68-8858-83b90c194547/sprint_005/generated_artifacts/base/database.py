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
    # Create the Course table
    Course.__table__.create(bind=engine, checkfirst=True)
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
    # Create the courses table if it does not exist
    with engine.connect() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                level TEXT NOT NULL
            )
        ''')
    # Ensure existing course data is preserved
    with engine.connect() as conn:
        existing_courses = conn.execute('SELECT * FROM courses').fetchall()
        if existing_courses:
            # Logic to handle existing courses if necessary
            pass
    # Create the student_courses association table
    with engine.connect() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS student_courses (
                student_id INTEGER,
                course_id INTEGER,
                PRIMARY KEY (student_id, course_id),
                FOREIGN KEY (student_id) REFERENCES students (id),
                FOREIGN KEY (course_id) REFERENCES courses (id)
            )
        ''')