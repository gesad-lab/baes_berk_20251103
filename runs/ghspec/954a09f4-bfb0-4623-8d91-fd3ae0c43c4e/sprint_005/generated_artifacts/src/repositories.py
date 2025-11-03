"""Create teachers table"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace xxxxxx with a unique revision ID
down_revision = 'previous_revision'  # Replace with the ID of the last migration

def upgrade():
    """Add the teachers table to the database."""
    op.create_table('teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )

def downgrade():
    """Remove the teachers table from the database."""
    op.drop_table('teachers')