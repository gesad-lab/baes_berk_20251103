'''
Migration script to add email column to the existing students table and create courses and teachers tables.
'''
from sqlalchemy import Column, String, Integer, ForeignKey
from alembic import op
def upgrade():
    # Step 1: Create the teachers table
    op.create_table(
        'teachers',
        Column('id', Integer, primary_key=True, index=True),
        Column('name', String, nullable=False),
        Column('email', String, nullable=False)
    )
    # Step 2: Create the courses table
    op.create_table(
        'courses',
        Column('id', Integer, primary_key=True, index=True),
        Column('name', String, nullable=False),
        Column('level', String, nullable=False),
        Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True)  # Add teacher_id column
    )
    # Step 3: Add the email column as nullable first to preserve existing data
    op.add_column('students', Column('email', String, nullable=True))
    # Step 4: Update existing records to set a default value for email
    op.execute("UPDATE students SET email = '' WHERE email IS NULL")
    # Step 5: Alter the email column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
    # Step 6: Create the new relationship table for students and courses
    op.create_table(
        'student_courses',
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
    )
    # Step 7: Migrate existing courses and assign teacher_id if applicable
    # This step assumes you have a way to determine which teacher corresponds to each course
    # For example, if you have a mapping or a default teacher, you can execute an update here
    # op.execute("UPDATE courses SET teacher_id = <default_teacher_id> WHERE teacher_id IS NULL")
def downgrade():
    op.drop_table('student_courses')
    op.drop_table('courses')
    op.drop_table('teachers')
    op.drop_column('students', 'email')