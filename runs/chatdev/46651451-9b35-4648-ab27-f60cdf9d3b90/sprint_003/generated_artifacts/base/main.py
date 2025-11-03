'''
Handles database migrations to add the email field to the Student entity.
'''
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from models import Base, Student
from sqlalchemy import text
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def upgrade():
    '''
    Adds the email column to the students table if it doesn't exist.
    '''
    with engine.connect() as connection:
        # Check if the column already exists
        result = connection.execute(text("PRAGMA table_info(students)"))
        columns = [row[1] for row in result]
        if 'email' not in columns:
            connection.execute('ALTER TABLE students ADD COLUMN email TEXT NOT NULL')
def downgrade():
    '''
    Logic to remove the email column if necessary (not implemented).
    '''
    pass
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  # Create tables if they don't exist
    upgrade()  # Run the upgrade to add the email field