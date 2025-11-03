from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from src.models.student import Student

def upgrade():
    engine = create_engine("sqlite:///./students.db")
    with engine.connect() as connection:
        # Add the new email column with NOT NULL constraint and default empty string
        connection.execute('ALTER TABLE students ADD COLUMN email TEXT NOT NULL DEFAULT "";')

def downgrade():
    # Logic to be defined if needing a rollback.
    # This should ideally remove the email field while considering the existing data, 
    # or at least prevent the column from being accessed after downgrade.
    pass

if __name__ == "__main__":
    upgrade()