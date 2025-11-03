'''
Migration script to add email column to the existing Student table.
'''
from sqlalchemy import create_engine, text
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
with engine.connect() as connection:
    # Allow email to be nullable initially
    connection.execute(text("ALTER TABLE students ADD COLUMN email TEXT;"))