'''
Database migration script to add email column to the existing Student table and create Course table.
'''
from sqlalchemy import create_engine, text  # Import text from SQLAlchemy
from models import Base, Course  # Import Base and Course to create tables
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
def create_tables():
    '''
    Create the database tables if they do not exist.
    '''
    Base.metadata.create_all(bind=engine)
def add_email_column():
    '''
    Add the email column to the students table if it does not already exist.
    '''
    with engine.connect() as connection:
        # Check if the column already exists
        result = connection.execute(text("PRAGMA table_info(students);"))  # Use text() here
        columns = [row[1] for row in result]
        if "email" not in columns:
            connection.execute(text("ALTER TABLE students ADD COLUMN email TEXT NOT NULL DEFAULT '';"))  # Use text() here
def create_course_table():
    '''
    Create the courses table in the database.
    '''
    Course.__table__.create(bind=engine, checkfirst=True)
if __name__ == "__main__":
    create_tables()  # Ensure tables are created before altering them
    add_email_column()
    create_course_table()  # Ensure the Course table is created