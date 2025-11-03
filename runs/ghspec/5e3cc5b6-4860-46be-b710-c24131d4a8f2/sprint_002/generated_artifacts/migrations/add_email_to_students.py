from sqlalchemy import create_engine, Column, String, MetaData, Table, alter
from sqlalchemy.exc import ProgrammingError

# Migration script to add email column to students table
DATABASE_URL = 'sqlite:///./test.db'  # Replace with your actual database URL
engine = create_engine(DATABASE_URL)

# Define metadata for the current database
metadata = MetaData(bind=engine)

# Reflect the existing students table
students_table = Table('students', metadata, autoload_with=engine)

def add_email_column():
    # Adding the 'email' column to the 'students' table
    with engine.connect() as conn:
        try:
            # Attempt to alter the table to add the email column
            alter_stmt = f'ALTER TABLE "{students_table.name}" ADD COLUMN email STRING NOT NULL'
            conn.execute(alter_stmt)
            print("Email column added successfully.")
        except ProgrammingError as e:
            # Handle error if the column already exists or there's an issue with the operation
            print(f"Error while adding email column: {e}")

if __name__ == "__main__":
    add_email_column()