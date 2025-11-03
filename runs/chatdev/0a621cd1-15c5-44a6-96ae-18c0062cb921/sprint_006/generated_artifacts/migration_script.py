'''
Migration script to add Teacher table and preserve existing Student and Course data.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '20231001_001'  # Example unique revision ID
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Add teacher_id column to the courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))
def downgrade():
    # Drop the teachers table if needed
    op.drop_table('teachers')
    # Drop the teacher_id column from the courses table
    op.drop_column('courses', 'teacher_id')