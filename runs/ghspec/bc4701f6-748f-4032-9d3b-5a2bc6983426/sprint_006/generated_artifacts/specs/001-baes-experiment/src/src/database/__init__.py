```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker

def initialize_database():
    # Create an engine instance connected to SQLite database
    engine = create_engine('sqlite:///app.db')
    metadata = MetaData()

    # Define the new column for teacher relationships in the existing courses table
    courses_table = Table('courses', metadata,
                          autoload_with=engine,  # Automatically load existing table structure
                          extend_existing=True)

    # Check if the teacher_id column already exists, if not, add it
    if 'teacher_id' not in courses_table.columns:
        # Define the column as a foreign key reference to teachers table
        teacher_id_column = Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True)
        courses_table.append_column(teacher_id_column)

    # Create or update tables including the new column
    metadata.create_all(engine)
```