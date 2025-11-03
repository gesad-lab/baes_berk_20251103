'''
Migration script to add email field to Student table.
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Student  # Importing the Student model
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def upgrade():
    """Add email column to the students table."""
    with engine.connect() as connection:
        # Add the email column allowing NULL values
        connection.execute('ALTER TABLE students ADD COLUMN email STRING')
        # Optionally, update existing records with a default email or handle them as needed
        # Example: connection.execute('UPDATE students SET email = "default@example.com" WHERE email IS NULL')
        # After ensuring all records have valid email, you can alter the column to NOT NULL if needed
        # This requires creating a new table and copying data, as SQLite does not support altering NOT NULL constraints directly.
def downgrade():
    """Remove email column from the students table if needed."""
    # Note: SQLite does not support dropping columns directly.
    # This would require creating a new table without the email column,
    # copying the data, and then dropping the old table.
    pass
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)