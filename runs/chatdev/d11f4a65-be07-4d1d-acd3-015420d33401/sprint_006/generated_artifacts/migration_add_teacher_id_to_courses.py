'''
Migration script to add teacher_id column to the courses table.
'''
from alembic import op
import sqlalchemy as sa
revision = 'unique_revision_id_4'  # Replace with a unique revision ID
down_revision = 'unique_revision_id'  # Ensure this is the last applied migration ID for courses
branch_labels = None
depends_on = None
def upgrade():
    # Add teacher_id column to the courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))
def downgrade():
    # Remove teacher_id column from the courses table
    op.drop_column('courses', 'teacher_id')