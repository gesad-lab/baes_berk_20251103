'''
Migration script to add email column to the existing Student table and create Course table.
'''
from sqlalchemy import create_engine, text
from models import Base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
def create_tables():
    '''
    Creates the necessary tables in the database, including the Course table.
    '''
    Base.metadata.create_all(engine)  # This will create both students and courses tables
def add_email_column():
    '''
    Adds the email column to the students table.
    The email column is added as nullable initially to preserve existing data.
    '''
    with engine.connect() as connection:
        # Check if the email column already exists
        result = connection.execute(text("PRAGMA table_info(students)"))
        columns = [row[1] for row in result]
        if 'email' not in columns:
            # Add email column as nullable initially to preserve existing data
            connection.execute(text("ALTER TABLE students ADD COLUMN email TEXT"))
        else:
            print("Email column already exists, skipping addition.")
if __name__ == "__main__":
    create_tables()  # Ensure tables are created before migration
    add_email_column()