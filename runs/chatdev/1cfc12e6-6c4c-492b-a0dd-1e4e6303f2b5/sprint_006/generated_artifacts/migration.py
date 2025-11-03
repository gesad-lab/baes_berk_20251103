'''
Database migration script to add Teacher entity and preserve existing Student and Course data.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with a unique revision ID
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # Create teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Add teacher_id column to courses table (make it nullable)
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))  # Change here
def downgrade():
    # Drop teachers table
    op.drop_table('teachers')
    # Drop teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')  # Add this line