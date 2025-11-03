'''
Handles the database migration for adding the Teacher table and updating the Course table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create the Teacher table if it doesn't exist
    if not op.get_bind().has_table('teachers'):
        op.create_table('teachers',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('email', sa.String(), nullable=False)
        )
    # Add the teacher_id column to the courses table if it doesn't exist
    if not op.get_bind().has_column('courses', 'teacher_id'):
        op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))
def downgrade():
    # Remove the teacher_id column if it exists
    if op.get_bind().has_column('courses', 'teacher_id'):
        op.drop_column('courses', 'teacher_id')
    # Drop the Teacher table if it exists
    if op.get_bind().has_table('teachers'):
        op.drop_table('teachers')