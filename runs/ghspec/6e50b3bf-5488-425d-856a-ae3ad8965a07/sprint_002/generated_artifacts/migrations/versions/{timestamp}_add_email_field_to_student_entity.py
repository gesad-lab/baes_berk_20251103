from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = '{timestamp}'  # Replace with actual timestamp
down_revision = None  # Set to the previous revision ID if there is one
branch_labels = None
depends_on = None


def upgrade():
    """Add email field to the student entity."""
    # Add the 'email' column to the 'students' table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))


def downgrade():
    """Remove email field from the student entity."""
    # Remove the 'email' column from the 'students' table
    op.drop_column('students', 'email')