```python
from sqlalchemy import create_engine, Table, Column, MetaData, Integer, String

def create_courses_table():
    """
    Create the courses table in the database if it does not exist.
    The courses table includes an id, name, and level fields.
    """
    # Use the existing database path
    engine = create_engine('sqlite:///database.db')
    metadata = MetaData(bind=engine)
    
    # Define the courses table schema
    courses_table = Table('courses', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String, nullable=False),  # Name field is required
        Column('level', String, nullable=False)  # Level field is required
    )
    
    # Create the table in the database
    metadata.create_all(engine)  # Creates the table if it doesn't exist

# Call the function to execute the migration
if __name__ == "__main__":
    create_courses_table()
```