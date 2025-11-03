'''
Migration script to add email field to Student entity and create Course and Teacher tables.
'''
from sqlalchemy import Column, String, Integer, Table, ForeignKey
from alembic import op
def upgrade():
    # Create a temporary table to hold existing courses
    op.create_table(
        'temp_courses',
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('level', String, nullable=False)
    )
    # Copy existing data into the temporary table
    op.execute('INSERT INTO temp_courses (id, name, level) SELECT id, name, level FROM courses')
    # Drop the original courses table
    op.drop_table('courses')
    # Create the teachers table
    op.create_table(
        'teachers',
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('email', String, nullable=False)
    )
    # Create the courses table with the new schema
    op.create_table(
        'courses',
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('level', String, nullable=False),
        Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True)  # Added teacher_id
    )
    # Restore data from the temporary table
    op.execute('INSERT INTO courses (id, name, level) SELECT id, name, level FROM temp_courses')
    # Drop the temporary table
    op.drop_table('temp_courses')
def downgrade():
    op.drop_table('student_courses')
    op.drop_table('courses')
    op.drop_table('teachers')