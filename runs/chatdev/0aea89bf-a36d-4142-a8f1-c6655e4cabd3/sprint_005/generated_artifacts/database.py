'''
Database connection and session management.
'''
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, ForeignKey
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
    Migrate the database to add the Teacher table and preserve existing data.
    '''
    metadata = MetaData(bind=engine)
    # Create the Teacher table if it doesn't exist
    teachers_table = Table('teachers', metadata)
    if not teachers_table.exists():
        with engine.connect() as connection:
            connection.execute('''
                CREATE TABLE teachers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')
    # Existing migration logic for students and courses
    students_table = Table('students', metadata, autoload_with=engine)
    if 'email' not in students_table.columns:
        with engine.connect() as connection:
            connection.execute(f'ALTER TABLE students ADD COLUMN email TEXT')
            connection.execute(f'UPDATE students SET email = "" WHERE email IS NULL')
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
    student_courses_table = Table(
        'student_courses',
        metadata,
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
    )
    if not student_courses_table.exists():
        with engine.connect() as connection:
            connection.execute('''
                CREATE TABLE student_courses (
                    student_id INTEGER,
                    course_id INTEGER,
                    PRIMARY KEY (student_id, course_id),
                    FOREIGN KEY (student_id) REFERENCES students (id),
                    FOREIGN KEY (course_id) REFERENCES courses (id)
                )
            ''')