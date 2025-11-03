'''
Migration script to add Teacher table to the database.
This script ensures that the Teacher table is created without affecting existing Student and Course data.
'''
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Teacher  # Import the Teacher model
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create the Teacher table if it does not exist
def create_teacher_table():
    inspector = inspect(engine)
    if 'teachers' not in inspector.get_table_names():
        Teacher.__table__.create(bind=engine)  # Create only the Teacher table
try:
    create_teacher_table()
except Exception as e:
    print(f"Error creating Teacher table: {e}")