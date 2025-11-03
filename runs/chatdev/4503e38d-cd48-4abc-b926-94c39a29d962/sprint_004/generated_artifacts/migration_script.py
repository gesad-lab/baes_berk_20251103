'''
Migration script to add email field to Student entity and create Course table.
'''
from sqlalchemy import Column, String, Integer, Table, ForeignKey
from alembic import op
def upgrade():
    # Step 1: Add the email column as nullable
    op.add_column('students', Column('email', String, nullable=True))
    # Step 2: (Optional) Populate existing records with a default value or leave as is
    # This step would require a separate SQL command to update existing records if needed.
    # Step 3: Alter the email column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
    # Create the Course table
    op.create_table(
        'courses',
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('level', String, nullable=False)
    )
    # Create a junction table for the many-to-many relationship
    op.create_table(
        'student_courses',
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    op.drop_table('student_courses')
    op.drop_table('courses')
    op.drop_column('students', 'email')