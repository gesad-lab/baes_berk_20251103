'''
Migration script to add teacher_id to Course table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '20231001_add_teacher_relationship'  # Update this to a unique revision ID
down_revision = '20231001_add_teacher'  # Ensure this matches the last applied migration ID
branch_labels = None
depends_on = None
def upgrade():
    """Add teacher_id column to the Course table."""
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))  # Allow NULL values for existing records
def downgrade():
    """Remove teacher_id column from the Course table."""
    op.drop_column('courses', 'teacher_id')