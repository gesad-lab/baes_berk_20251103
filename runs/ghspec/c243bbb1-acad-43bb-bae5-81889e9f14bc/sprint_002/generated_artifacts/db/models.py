from sqlalchemy import create_engine, MetaData, Table, Column, String

# Define the database engine using SQLite
engine = create_engine('sqlite:///students.db')
metadata = MetaData(bind=engine)

# Load the existing 'students' table from the database
students = Table('students', metadata, autoload_with=engine)

# Begin a migration session to add the 'email' column to the 'students' table
with engine.begin() as connection:
    # Execute the SQL command to add a new column 'email' of type VARCHAR and not nullable
    connection.execute(f'ALTER TABLE {students.name} ADD COLUMN email VARCHAR NOT NULL')