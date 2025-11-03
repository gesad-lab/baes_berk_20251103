# /src/database/migrations/add_email_to_students.py

from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = '2023121501'
down_revision = None  # Adjust based on your migration history
branch_labels = None
depends_on = None


def upgrade():
    """Add 'email' column to 'students' table."""
    # Add the 'email' column to the 'students' table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))


def downgrade():
    """Remove 'email' column from 'students' table."""
    # Drop the 'email' column if we need to downgrade the migration
    op.drop_column('students', 'email')