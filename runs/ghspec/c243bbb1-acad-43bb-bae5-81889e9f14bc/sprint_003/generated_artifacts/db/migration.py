```python
# db/migration.py

from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer

# Create a SQLite database engine
engine = create_engine('sqlite:///courses.db')
metadata = MetaData(bind=engine)

# Define the courses table with required columns
courses_table = Table('courses', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False),  # Course name must be provided
    Column('level', String, nullable=False)  # Course level must be provided
)

# Create all defined tables. If they already exist, they will be ignored.
metadata.create_all(engine)  # Creates the 'courses' table in the database
```