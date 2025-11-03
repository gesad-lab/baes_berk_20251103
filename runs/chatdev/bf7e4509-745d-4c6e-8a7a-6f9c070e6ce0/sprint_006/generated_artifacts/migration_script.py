'''
Migration script to add Teacher entity to the database.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with a unique revision ID
down_revision = None  # Replace with the previous revision ID if applicable
branch_labels = None
depends_on = None
def upgrade():
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
    )
    # Add teacher_id column to courses table with a default value
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))  # Allow NULL for existing records
def downgrade():
    # Remove the teachers table if needed
    op.drop_table('teachers')
    # Remove teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')  # Add this line to drop the column if needed