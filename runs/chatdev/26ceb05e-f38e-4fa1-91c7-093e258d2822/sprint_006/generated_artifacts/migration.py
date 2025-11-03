'''
Migration script to add the Teacher table to the database while preserving existing data.
'''
from sqlalchemy import create_engine, inspect, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from models import Base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
# Check if the Teacher table already exists
if not inspect(engine).has_table("teachers"):
    # Create the Teacher table if it does not exist
    Base.metadata.create_all(bind=engine, tables=[Base.metadata.tables['teachers']])
# Check if the teacher_id column exists in the Course table
if not inspect(engine).has_column("courses", "teacher_id"):
    with SessionLocal() as session:
        # Add the teacher_id column to the Course table
        with engine.connect() as connection:
            connection.execute('ALTER TABLE courses ADD COLUMN teacher_id INTEGER;')