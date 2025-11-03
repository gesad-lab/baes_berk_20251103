'''
Database migration script for adding Teacher table and Course-Teacher relationship.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'unique_revision_id'  # Replace with a unique revision ID
down_revision = None  # Replace with the previous revision ID if applicable
branch_labels = None
depends_on = None
def upgrade():
    # Create the Teacher table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
    )
    # Add teacher_id column to courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))
    # Optional: Set a default teacher_id for existing courses if applicable
    # This assumes you have a default teacher to associate with existing courses
    op.execute("UPDATE courses SET teacher_id = (SELECT id FROM teachers LIMIT 1) WHERE teacher_id IS NULL")
def downgrade():
    # Drop the teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')
    # Drop the Teacher table if needed
    op.drop_table('teachers')