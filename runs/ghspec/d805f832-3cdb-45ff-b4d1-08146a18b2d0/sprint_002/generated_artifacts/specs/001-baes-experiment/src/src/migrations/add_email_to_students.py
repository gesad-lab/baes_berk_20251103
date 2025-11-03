from sqlalchemy import create_engine, Column, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from models import Base  # Assuming Base is defined in models.py

# Database configuration
DATABASE_URL = "sqlite:///./database.db"  # Update with your actual database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Migration function to add email column to the students table
def add_email_column_to_students():
    # Bind the metadata to the engine
    Base.metadata.bind = engine

    # Connect to the database
    with engine.connect() as connection:
        # Execute SQL to add the new column
        try:
            connection.execute('ALTER TABLE students ADD COLUMN email STRING NOT NULL DEFAULT "";')
        except IntegrityError as e:
            # Log the error for debugging but do not expose it to users
            print("Migration failed:", str(e))
            raise RuntimeError("Failed to add 'email' column to 'students' table. Please check the logs.")

if __name__ == "__main__":
    add_email_column_to_students()  # Execute the migration when run directly