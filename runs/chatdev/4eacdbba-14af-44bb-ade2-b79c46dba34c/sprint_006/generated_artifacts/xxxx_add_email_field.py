'''
Migration script to add email field to Student entity, create Course table, and create Teacher table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Add the email column as nullable first to preserve existing data
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))  # Change to nullable=False
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'))  # Add this line
    )
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True)
    )
    op.create_table(  # New table for Teacher
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
def downgrade():
    op.drop_table('student_courses')
    op.drop_table('courses')
    op.drop_table('teachers')  # Drop Teacher table on downgrade
    op.drop_column('students', 'email')  # Drop email column on downgrade