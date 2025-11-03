'''
Migration script to add email field to Student entity.
'''
from sqlalchemy import Column, String, Integer, create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from database import init_db  # Importing init_db to ensure database initialization
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)  # Changed to nullable initially
def upgrade():
    '''
    Adds the email column to the existing Student table and updates existing records.
    '''
    with engine.connect() as connection:
        # Check if the students table exists before altering
        result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='students';"))
        if result.fetchone() is not None:
            # Add email column as nullable first
            connection.execute(text('ALTER TABLE students ADD COLUMN email TEXT'))  # Wrapped in text()
            # Update existing records with a default value to comply with the required field
            connection.execute(text('UPDATE students SET email = "default@example.com" WHERE email IS NULL'))  # Wrapped in text()
        else:
            print("Table 'students' does not exist. Please create the table first.")
def downgrade():
    '''
    Removes the email column from the Student table if needed.
    '''
    with engine.connect() as connection:
        connection.execute(text('ALTER TABLE students DROP COLUMN email'))  # Wrapped in text()
if __name__ == "__main__":
    init_db()  # Ensure the database and tables are created first
    upgrade()  # Then run the upgrade to add the email field