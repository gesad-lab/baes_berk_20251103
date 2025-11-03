'''
Migration script to add Teacher entity and ensure Student data is preserved.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    '''
    Upgrade the database schema to include the teachers table and ensure existing data is preserved.
    '''
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )
    # Add the teacher_id column to the courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id')))  # Add this line
def downgrade():
    '''
    Downgrade the database schema by dropping the association table and the teachers table.
    '''
    op.drop_table('teachers')
    op.drop_column('courses', 'teacher_id')  # Remove the teacher_id column