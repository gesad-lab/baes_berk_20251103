```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey

def initialize_database():
    engine = create_engine('sqlite:///app.db')
    metadata = MetaData()

    # Define courses table structure
    courses_table = Table('courses', metadata,
                          Column('id', Integer, primary_key=True),
                          # Adding the new teacher_id foreign key column for teacher relationships
                          Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True)
                          )

    # Create or update tables including the new teacher_id column
    metadata.create_all(engine)

if __name__ == "__main__":
    initialize_database()  # Run the migration logic on script execution
```