'''
Migration script to create teachers table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '20231001_03'  # Update with a new unique revision ID
down_revision = '20231001_02'  # Update with the previous migration revision ID
branch_labels = None
depends_on = None
def upgrade():
    '''
    Create teachers table.
    '''
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
    )
def downgrade():
    '''
    Drop teachers table.
    '''
    op.drop_table('teachers')