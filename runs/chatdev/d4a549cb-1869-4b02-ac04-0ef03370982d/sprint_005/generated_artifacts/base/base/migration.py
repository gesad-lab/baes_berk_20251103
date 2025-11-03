'''
Migration script to add Course table and email field to the Student table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with your revision ID
down_revision = None  # Replace with your previous revision ID
branch_labels = None
depends_on = None
def upgrade():
    # Add email column to students table, make it nullable to preserve existing data
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('level', sa.String, nullable=False)
    )
def downgrade():
    # Drop courses table
    op.drop_table('courses')
    # Drop email column from students table
    op.drop_column('students', 'email')