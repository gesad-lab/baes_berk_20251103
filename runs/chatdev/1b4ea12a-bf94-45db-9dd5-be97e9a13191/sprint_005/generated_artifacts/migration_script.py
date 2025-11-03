'''
Migration script to create Course table, Teacher table, and the association table for students and courses.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    '''
    Create the courses table, teachers table, and the association table for students and courses.
    Ensure existing data is preserved.
    '''
    # Check if the courses table already exists
    if not op.get_bind().has_table('courses'):
        op.create_table(
            'courses',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('level', sa.String(), nullable=False),
        )
    # Check if the teachers table already exists
    if not op.get_bind().has_table('teachers'):
        op.create_table(
            'teachers',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('email', sa.String(), nullable=False),
        )
    # Check if the student_courses table already exists
    if not op.get_bind().has_table('student_courses'):
        op.create_table(
            'student_courses',
            sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
            sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True),
        )
def downgrade():
    '''
    Drop the courses table, teachers table, and the association table for students and courses.
    '''
    op.drop_table('student_courses')
    op.drop_table('courses')
    op.drop_table('teachers')