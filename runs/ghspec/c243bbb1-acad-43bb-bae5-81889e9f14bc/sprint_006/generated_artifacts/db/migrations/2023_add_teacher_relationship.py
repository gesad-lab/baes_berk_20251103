```python
# db/migrations/2023_add_teacher_relationship.py

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey

# Creating a SQLite engine for the database
engine = create_engine('sqlite:///courses.db')
metadata = MetaData(bind=engine)

def upgrade():
    """Add teacher_id column to the courses table with foreign key constraint."""
    courses_table = Table('courses', metadata, autoload_with=engine)

    # Check if the teacher_id column already exists to avoid errors
    if 'teacher_id' not in courses_table.columns:
        # Adding teacher_id column to the existing courses table
        teacher_id_column = Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True)
        teacher_id_column.create(courses_table)

def downgrade():
    """Remove teacher_id column from the courses table if it exists."""
    courses_table = Table('courses', metadata, autoload_with=engine)

    # Check if the teacher_id column exists before trying to drop it
    if 'teacher_id' in courses_table.columns:
        teacher_id_column = courses_table.c.teacher_id
        teacher_id_column.drop()
```