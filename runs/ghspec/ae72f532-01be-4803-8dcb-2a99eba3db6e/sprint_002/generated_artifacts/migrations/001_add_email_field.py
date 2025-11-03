from sqlalchemy import.Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Define the base declarative class
Base = declarative_base()

class Student(Base):
    """Represents a student in the database."""
    
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field added

# Database setup
DATABASE_URL = "sqlite:///students.db"  # Example database URL
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Create a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def add_email_field():
    """Migration to add the email field to the students table."""
    with SessionLocal() as session:
        # Check if the email field already exists in the database
        if not engine.dialect.has_table(engine, 'students'):
            print("No students table found. Please ensure the database exists.")
            return

        # Perform the migration to add email field
        # Note: You should implement this using Alembic for production and safety reasons.
        try:
            # Here you should add the SQL for altering the table. This is a placeholder approach.
            session.execute('ALTER TABLE students ADD COLUMN email STRING NOT NULL')
            session.commit()
        except Exception as e:
            print(f"Error during migration: {e}")
            session.rollback()

if __name__ == '__main__':
    add_email_field()  # Call the function to add the email field when running this script.