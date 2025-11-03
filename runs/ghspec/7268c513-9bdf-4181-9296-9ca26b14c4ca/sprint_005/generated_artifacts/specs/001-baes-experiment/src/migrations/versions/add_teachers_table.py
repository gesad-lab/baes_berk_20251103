from alembic import op
import sqlalchemy as sa

# Migration script to add the `teachers` table to the existing database schema.

def upgrade():
    """Create the `teachers` table in the database."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False)
    )

def downgrade():
    """Drop the `teachers` table from the database."""
    op.drop_table('teachers')