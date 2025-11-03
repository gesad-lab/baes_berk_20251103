```python
# db/student_courses_model.py

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey

# Initialize the database engine
# File: db/student_courses_model.py
engine = create_engine('sqlite:///courses.db')

# Create metadata instance
metadata = MetaData(bind=engine)

# Define the student_courses join table
student_courses_table = Table('student_courses', metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

# Create the table in the database if it does not exist
if not engine.dialect.has_table(engine, 'student_courses'):
    metadata.create_all(engine)  # Creates the table
```