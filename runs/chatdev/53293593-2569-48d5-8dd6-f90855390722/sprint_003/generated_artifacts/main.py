'''
Handles database migrations to add the email field to the Student entity and create the Course table.
'''
from sqlalchemy import create_engine, Column, String, Integer, text  # Added text import
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import MetaData
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field
# Create a new migration
def migrate():
    metadata = MetaData()
    metadata.reflect(bind=engine)  # Reflect the current database schema
    # Migrate Student table
    if 'students' in metadata.tables:
        with engine.connect() as connection:
            # Step 1: Create a new table with the email column
            connection.execute(text('CREATE TABLE students_new (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL)'))  # Wrapped in text()
            # Step 2: Copy existing records to the new table, including the email
            connection.execute(text('INSERT INTO students_new (id, name, email) SELECT id, name, email FROM students'))  # Wrapped in text()
            # Step 3: Drop the old table
            connection.execute(text('DROP TABLE students'))  # Wrapped in text()
            # Step 4: Rename the new table to the original name
            connection.execute(text('ALTER TABLE students_new RENAME TO students'))  # Wrapped in text()
    # Add migration for Course table
    if 'courses' not in metadata.tables:
        with engine.connect() as connection:
            connection.execute(text('CREATE TABLE courses (id INTEGER PRIMARY KEY, name TEXT NOT NULL, level TEXT NOT NULL)'))  # Wrapped in text()
if __name__ == "__main__":
    migrate()