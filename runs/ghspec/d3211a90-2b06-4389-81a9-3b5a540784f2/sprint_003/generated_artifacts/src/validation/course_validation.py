```python
from sqlalchemy import create_engine, Table, Column, MetaData, Integer, String

def create_courses_table():
    """
    Creates the 'courses' table in the database with the fields id, name, and level.
    The 'name' and 'level' fields are both required strings.
    """
    engine = create_engine('sqlite:///database.db')  # Ensure this matches the existing database path
    metadata = MetaData(bind=engine)
    
    courses_table = Table('courses', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String, nullable=False),  # Name is a required string
        Column('level', String, nullable=False)  # Level is a required string
    )
    
    # Create table if it does not exist
    metadata.create_all(engine)  
```