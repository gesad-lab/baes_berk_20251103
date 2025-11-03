'''
Migration script to create courses table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Update with a new revision ID
down_revision = 'xxxxxx'  # Update with the previous migration revision ID
branch_labels = None
depends_on = None
def upgrade():
    '''
    Create courses table.
    '''
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )
def downgrade():
    '''
    Drop courses table.
    '''
    op.drop_table('courses')