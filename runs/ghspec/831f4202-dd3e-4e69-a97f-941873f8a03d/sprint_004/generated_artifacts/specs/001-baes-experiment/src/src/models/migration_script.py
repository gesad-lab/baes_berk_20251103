from sqlalchemy import create_engine, Column, ForeignKey, Integer, Table, MetaData, inspect

def add_student_courses_table():
    # Create engine to connect to the SQLite database
    engine = create_engine('sqlite:///app.db')
    metadata = MetaData()

    # Define the 'student_courses' junction table for many-to-many relationship
    student_courses_table = Table('student_courses', metadata,
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
    )
    
    # Check if the table already exists to avoid conflicts
    inspector = inspect(engine)
    if 'student_courses' not in inspector.get_table_names():
        metadata.create_all(engine)  # Create the junction table only if it doesn't exist
    else:
        print("Table 'student_courses' already exists. No changes made.")

# Call the function to apply the migration
if __name__ == "__main__":
    add_student_courses_table()  # Execute the migration on script run