```python
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String

def add_courses_table():
    # Establish connection to the SQLite database
    engine = create_engine('sqlite:///app.db')
    metadata = MetaData()

    # Define the new 'courses' table with required fields
    courses_table = Table('courses', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String, nullable=False),  # Course name must not be null
        Column('level', String, nullable=False)  # Course level must not be null
    )

    # Create the new table in the database
    metadata.create_all(engine)
```