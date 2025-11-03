'''
Migration script for adding the Teacher table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create the Teacher table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False)
    )
def downgrade():
    # Drop the Teacher table
    op.drop_table('teachers')