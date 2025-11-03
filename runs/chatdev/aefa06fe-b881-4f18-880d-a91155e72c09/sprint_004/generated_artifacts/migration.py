'''
Migration script to add email column to the existing students table and create courses table.
'''
from sqlalchemy import Column, String, Integer, ForeignKey
from alembic import op
def upgrade():
    # Step 1: Create the courses table
    op.create_table(
        'courses',
        Column('id', Integer, primary_key=True, index=True),
        Column('name', String, nullable=False),
        Column('level', String, nullable=False)
    )
    # Step 2: Add the email column as nullable first
    op.add_column('students', Column('email', String, nullable=True))
    # Step 3: Update existing records to set a default value for email
    op.execute("UPDATE students SET email = '' WHERE email IS NULL")
    # Step 4: Alter the email column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
    # Step 5: Create the new relationship table for students and courses
    op.create_table(
        'student_courses',
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    op.drop_table('student_courses')
    op.drop_table('courses')
    op.drop_column('students', 'email')