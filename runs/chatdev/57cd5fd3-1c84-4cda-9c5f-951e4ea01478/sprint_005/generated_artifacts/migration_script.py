'''
Alembic migration script to add Teacher table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create the Teacher table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
    )
    # Check if the courses table already exists before creating it
    if not op.get_bind().has_table('courses'):
        op.create_table(
            'courses',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('level', sa.String(), nullable=False),
        )
    # Create the association table if it doesn't exist
    if not op.get_bind().has_table('student_courses'):
        op.create_table(
            'student_courses',
            sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
            sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True),
        )
def downgrade():
    op.drop_table('student_courses')
    op.drop_table('courses')
    op.drop_table('teachers')