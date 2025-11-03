'''
Alembic migration script to add Course table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create the Course table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )
    # Ensure that existing Student data is preserved
    # Note: This migration does not alter the Student table, hence no data loss will occur.
def downgrade():
    op.drop_table('courses')