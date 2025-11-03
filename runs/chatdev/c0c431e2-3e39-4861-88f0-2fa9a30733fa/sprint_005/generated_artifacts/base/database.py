'''
Handles database connections and session management.
'''
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
# Import models after defining Base to avoid circular import
from models import student_courses  
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
    Migrates the database to add the email column to the Student table and create the Course table.
    '''
    metadata = MetaData(bind=engine)
    # Check if the students table exists
    if 'students' in metadata.tables:
        students_table = Table('students', metadata, autoload_with=engine)
        # Check if the email column already exists
        if 'email' not in students_table.columns:
            with engine.connect() as connection:
                # Add the email column as nullable first
                connection.execute('ALTER TABLE students ADD COLUMN email STRING')
                # Then update existing records to have a default value or handle accordingly
                connection.execute('UPDATE students SET email = "default@example.com" WHERE email IS NULL')
                # Finally, alter the column to be NOT NULL
                connection.execute('ALTER TABLE students RENAME TO students_temp')
                connection.execute('CREATE TABLE students (id INTEGER PRIMARY KEY, name STRING NOT NULL, email STRING NOT NULL)')
                connection.execute('INSERT INTO students (id, name, email) SELECT id, name, email FROM students_temp')
                connection.execute('DROP TABLE students_temp')
    else:
        print("The 'students' table does not exist.")
    # Create the courses table if it does not exist
    if 'courses' not in metadata.tables:
        Course.__table__.create(bind=engine)
    # Create the association table if it does not exist
    if 'student_courses' not in metadata.tables:
        student_courses.create(bind=engine)
def get_db() -> Session:
    '''
    Provides a database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()