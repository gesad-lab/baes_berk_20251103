```python
# migrations/add_student_courses_table.py

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey

# Database setup - adjust connection as needed
engine = create_engine('sqlite:///courses.db')
metadata = MetaData(bind=engine)

# Define the student_courses join table
student_courses_table = Table('student_courses', metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

def migrate():
    """
    Run the migration to create the student_courses table.
    This function is invoked to apply the schema changes to the database.
    """
    try:
        # Create the student_courses table if it doesn't already exist
        metadata.create_all(engine)
        print("Migration successful: student_courses table created.")
    except Exception as e:
        print(f"Migration failed: {e}")
        # It's crucial to log detailed error context during migration for debugging
        raise

if __name__ == '__main__':
    migrate()
```