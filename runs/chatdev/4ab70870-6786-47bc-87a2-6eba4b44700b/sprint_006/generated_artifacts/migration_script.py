'''
Database migration script for adding email field to Student entity, creating Course table, and creating Teacher table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create the teachers table first
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)  # Added email field with unique constraint
    )
    # Create the courses table with a foreign key to teachers
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True)  # Added foreign key for teacher
    )
    # Create the association table for the many-to-many relationship
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )
    # Add the new email column to students
    op.add_column('students', sa.Column('email', sa.String(), nullable=False, unique=True))
    # Update existing records to have a specific email format or unique value only if email is NULL
    op.execute("UPDATE students SET email='student_' || id || '@example.com' WHERE email IS NULL")
    # Set a default teacher_id for existing courses if needed
    # This assumes you have at least one teacher in the teachers table
    op.execute("""
        UPDATE courses 
        SET teacher_id = (SELECT id FROM teachers LIMIT 1) 
        WHERE teacher_id IS NULL
    """)
def downgrade():
    op.drop_table('student_courses')
    op.drop_table('courses')
    op.drop_table('teachers')  # Drop teachers table on downgrade
    op.drop_column('students', 'email')