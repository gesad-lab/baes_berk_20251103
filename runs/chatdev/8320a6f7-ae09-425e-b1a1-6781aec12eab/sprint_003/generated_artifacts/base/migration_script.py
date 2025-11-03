'''
Handles the migration of the Student table to add the email field.
'''
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
# Create a session
session = SessionLocal()
# Use MetaData to reflect the existing database
metadata = MetaData(bind=engine)
metadata.reflect()
# Get the existing Student table
students_table = Table('students', metadata, autoload_with=engine)
# Check if the email column already exists
if 'email' not in students_table.columns:
    # Add the email column to the existing table with a default value
    with engine.connect() as connection:
        connection.execute('ALTER TABLE students ADD COLUMN email TEXT NOT NULL DEFAULT ""')
# Commit the changes
session.commit()
session.close()