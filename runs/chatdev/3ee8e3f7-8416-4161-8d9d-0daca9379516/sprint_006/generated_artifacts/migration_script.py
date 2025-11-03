'''
Migration script to add Teacher table and preserve existing data.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '20231001_002'  # Use a timestamp or a unique identifier
down_revision = '20231001_001'
branch_labels = None
depends_on = None
def upgrade():
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True),  # Ensure email is unique
    )
    # Add teacher_id column to courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))  # Allow NULL initially
    # Optionally, if you want to set a default teacher for existing courses, you can do so here
    # Example: op.execute("UPDATE courses SET teacher_id = (SELECT id FROM teachers LIMIT 1) WHERE teacher_id IS NULL")
def downgrade():
    # Remove the teachers table if needed
    op.drop_table('teachers')
    # Remove teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')