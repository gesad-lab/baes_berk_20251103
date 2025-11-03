from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '<timestamp>_add_teachers_table'
down_revision = None  # Update accordingly if this is not the first migration
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create teachers table."""
    # Create a new table for teachers with the specified fields
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False),
    )


def downgrade() -> None:
    """Drop teachers table."""
    # Drop the teachers table when downgrading the migration
    op.drop_table('teachers')