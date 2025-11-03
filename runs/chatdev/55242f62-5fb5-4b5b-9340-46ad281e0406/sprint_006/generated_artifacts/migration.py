'''
Migration script to add teacher_id to Course entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '20231001_003'  # Unique revision ID for adding teacher_id
down_revision = '20231001_002'  # Replace with the correct previous revision ID
branch_labels = None
depends_on = None
def upgrade():
    # Add teacher_id column as nullable initially
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))  # Add foreign key for Teacher
    # Optionally, you can set a default value for existing records if needed
    # op.execute("UPDATE courses SET teacher_id = NULL WHERE teacher_id IS NULL")
def downgrade():
    op.drop_column('courses', 'teacher_id')  # Remove teacher_id column if needed