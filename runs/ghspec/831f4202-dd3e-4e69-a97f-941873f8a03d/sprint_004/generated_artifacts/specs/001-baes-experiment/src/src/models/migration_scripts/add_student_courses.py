```python
from sqlalchemy import create_engine, Column, ForeignKey, Integer, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creating a base class for SQLAlchemy models
Base = declarative_base()

def add_student_courses_table():
    """
    Creates the student_courses junction table to establish a many-to-many
    relationship between students and courses in the database.
    """
    engine = create_engine('sqlite:///app.db')  # Connects to the SQLite database
    metadata = MetaData()

    # Define the student_courses junction table
    student_courses_table = Table('student_courses', metadata,
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
    )
    
    # Create the junction table in the database
    try:
        metadata.create_all(engine)  # Executes the creation of the table
    except Exception as e:
        # Logging the error for debugging purposes
        print(f"Error creating student_courses table: {e}")
        raise  # Re-raise the exception for further handling

    print("student_courses table created successfully.")
```