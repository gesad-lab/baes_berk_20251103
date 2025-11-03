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
    # Create the Teacher table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False)
    )
def downgrade():
    # Drop the Teacher table if needed
    op.drop_table('teachers')