from sqlalchemy import create_engine, MetaData, Table, Column, String

# Create an engine to connect to the SQLite database
engine = create_engine('sqlite:///students.db')

# Create a MetaData instance to hold information about the database schema
metadata = MetaData(bind=engine)

# Load the existing students table schema
students = Table('students', metadata, autoload_with=engine)

# Create a migration script to add the 'email' column to the students table
with engine.begin() as connection:
    # Adding the 'email' column to the existing 'students' table
    connection.execute(f'ALTER TABLE {students.name} ADD COLUMN email VARCHAR NOT NULL')