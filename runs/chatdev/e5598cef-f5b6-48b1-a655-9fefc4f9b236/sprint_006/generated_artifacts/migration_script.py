'''
Database migration script to add Teacher table and preserve existing data.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)  # Ensure email is unique
    )
    # Add teacher_id column to courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))
def downgrade():
    # Drop teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')
    # Drop the teachers table
    op.drop_table('teachers')