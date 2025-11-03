'''
Migration script to add Teacher entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '20231001_002'  # Unique revision ID for Teacher addition
down_revision = 'xxxxxx'  # Replace with the correct previous revision ID
branch_labels = None
depends_on = None
def upgrade():
    # Create Teacher table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
def downgrade():
    # Remove Teacher table
    op.drop_table('teachers')