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
def downgrade():
    # Remove the teachers table if needed
    op.drop_table('teachers')