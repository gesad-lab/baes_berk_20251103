'''
Handles database migrations for the application.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    '''
    Upgrade the database schema to include the new Teacher table and the teacher_id column in courses.
    '''
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
    )
    # Add the teacher_id column to courses table, allowing nulls initially
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))  # Allow nulls initially
def downgrade():
    '''
    Downgrade the database schema by dropping the Teacher table and the teacher_id column in courses.
    '''
    op.drop_column('courses', 'teacher_id')  # Add this line
    op.drop_table('teachers')