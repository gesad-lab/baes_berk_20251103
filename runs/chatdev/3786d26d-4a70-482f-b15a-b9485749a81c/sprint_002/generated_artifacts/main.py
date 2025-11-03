'''
Migration script to add email column to the existing Student table.
'''
from sqlalchemy import create_engine, text  # Import text function
from models import Base  # Import Base from models.py
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# Create the tables in the database
Base.metadata.create_all(engine)  # This will create the students table if it doesn't exist
# Migration function
def migrate():
    with engine.connect() as connection:
        # Check if the email column already exists
        result = connection.execute(text("PRAGMA table_info(students);"))
        columns = [row[1] for row in result.fetchall()]
        if 'email' not in columns:
            connection.execute(text('ALTER TABLE students ADD COLUMN email TEXT;'))  # Add email column if it doesn't exist
if __name__ == "__main__":
    migrate()