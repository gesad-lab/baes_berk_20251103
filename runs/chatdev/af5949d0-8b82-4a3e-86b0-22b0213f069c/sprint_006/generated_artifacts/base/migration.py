'''
Migration script to add Teacher table and ensure existing data is preserved.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with a unique revision ID
down_revision = None  # Replace with the previous revision ID if applicable
branch_labels = None
depends_on = None
def upgrade():
    # Step 1: Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Step 2: Ensure existing data in Student and Course tables is preserved
    # (No action needed here as we are just adding a new table)
def downgrade():
    # Remove the teachers table
    op.drop_table('teachers')