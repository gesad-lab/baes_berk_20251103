'''
Migration script to add Course entity and its fields.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with actual revision ID
down_revision = 'yyyyyy'  # Replace with actual down revision ID
branch_labels = None
depends_on = None
def upgrade():
    # Create courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
def downgrade():
    # Drop courses table
    op.drop_table('courses')