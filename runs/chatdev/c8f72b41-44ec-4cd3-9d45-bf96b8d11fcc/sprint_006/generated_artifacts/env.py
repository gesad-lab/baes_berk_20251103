'''
Migration script for adding the Teacher table to the database.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with a unique revision ID
down_revision = None  # Replace with the previous revision ID if applicable
branch_labels = None
depends_on = None
def upgrade():
    # Check if the Teacher table already exists
    if not op.get_bind().has_table('teachers'):
        # Create the Teacher table
        op.create_table(
            'teachers',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String, nullable=False),
            sa.Column('email', sa.String, nullable=False)
        )
    # Add teacher_id column to Course table with a default value of NULL
    if not op.get_bind().has_column('courses', 'teacher_id'):
        op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))
def downgrade():
    # Check if the teacher_id column exists before dropping it
    if op.get_bind().has_column('courses', 'teacher_id'):
        op.drop_column('courses', 'teacher_id')
    # Check if the Teacher table exists before dropping it
    if op.get_bind().has_table('teachers'):
        op.drop_table('teachers')