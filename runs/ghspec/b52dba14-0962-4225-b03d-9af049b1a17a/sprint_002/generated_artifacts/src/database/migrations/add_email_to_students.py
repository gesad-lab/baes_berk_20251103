from sqlalchemy import create_engine, MetaData, Table, Column, String

def upgrade():
    # Create a connection to the SQLite database
    engine = create_engine('sqlite:///path_to_your_db')  # Update the path according to your setup
    metadata = MetaData(bind=engine)
    
    # Reflect the existing students table
    students = Table('students', metadata, autoload_with=engine)
    
    # Add the new 'email' column. Email must be a non-null string.
    with engine.connect() as connection:
        connection.execute("ALTER TABLE students ADD COLUMN email TEXT NOT NULL;")

def downgrade():
    # Downgrade logic to revert the schema changes if necessary
    # This may involve more complex logic such as creating a new table and migrating existing data,
    # since SQLite does not support dropping columns directly.
    pass  # Placeholder for future implementation if needed.