```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from your_application import db  # Adjust import based on your structure

def migrate_database():
    # Create an engine to manage the SQLite database connection
    engine = create_engine('sqlite:///your_database.db')
    metadata = MetaData()

    # Define the new teachers table schema
    teachers = Table(
        'teachers',
        metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String, nullable=False),
        Column('email', String, unique=True, nullable=False)
    )

    # Create the teachers table if it doesn't exist
    metadata.create_all(engine)

    # Ensure that existing data in other tables remains intact
    # Note: This method does not drop or modify existing tables

if __name__ == "__main__":
    migrate_database()
```