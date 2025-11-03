```python
from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from your_application.models import db  # Import the existing database instance

def migrate_create_student_courses_table():
    """
    This function creates a `student_courses` junction table to establish a 
    many-to-many relationship between the Student and Course entities.

    The table will include foreign keys linking to the Student and Course 
    tables, maintaining referential integrity.
    """
    # Create the engine using the configured database URL
    engine = create_engine('sqlite:///database.db')  # Adjust database URL as required
    connection = engine.connect()

    try:
        # Create the junction table for the many-to-many relationship
        connection.execute(
            """
            CREATE TABLE student_courses (
                student_id INTEGER,
                course_id INTEGER,
                PRIMARY KEY (student_id, course_id),
                FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE,
                FOREIGN KEY(course_id) REFERENCES courses(id) ON DELETE CASCADE
            );
            """
        )
    except Exception as e:
        # Log the error and re-raise for further handling
        print(f"An error occurred while creating the student_courses table: {e}")
        raise
    finally:
        # Ensure the connection is closed regardless of success or failure
        connection.close()
```