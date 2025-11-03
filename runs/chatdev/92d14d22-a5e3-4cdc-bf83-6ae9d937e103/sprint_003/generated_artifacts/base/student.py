'''
Migration script to add email column to Student table.
'''
from sqlalchemy import create_engine, Column, String, MetaData, Table
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData(bind=engine)
# Reflect the existing table
students_table = Table('students', metadata, autoload_with=engine)
# Add the new column
with engine.connect() as connection:
    connection.execute('ALTER TABLE students ADD COLUMN email TEXT NOT NULL DEFAULT ""')  # Set default value for existing records