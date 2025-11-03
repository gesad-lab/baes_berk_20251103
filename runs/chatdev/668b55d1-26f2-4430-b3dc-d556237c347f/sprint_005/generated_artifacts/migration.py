'''
Database migration script to add email field to Student entity, create Course table, and create Teacher table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Step 1: Add the email column to the students table as required
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
    # Step 2: Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
    # Step 3: Create the association table for students and courses
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True)
    )
    # Step 4: Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
def downgrade():
    op.drop_table('student_courses')
    op.drop_table('courses')
    op.drop_table('teachers')
    op.drop_column('students', 'email')