```python
# db/migrations/add_teacher_table.py

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Creating a SQLite engine for the database
engine = create_engine('sqlite:///courses.db')
metadata = MetaData(bind=engine)

def add_teacher_table():
    """Creates the teachers table in the database if it doesn't already exist."""
    # Define the teachers table structure
    teachers_table = Table('teachers', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String, nullable=False),
        Column('email', String, nullable=False)
    )

    # Create the table in the database
    metadata.create_all(engine)  # This will create the table if it does not exist

if __name__ == "__main__":
    add_teacher_table()
```