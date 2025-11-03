from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'unique_revision_id'  # Replace with the actual revision ID
down_revision = 'previous_revision_id'  # Replace with the previous revision ID
branch_labels = None
depends_on = None

def upgrade():
    """Add the email column to the students table."""
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    """Remove the email column from the students table."""
    op.drop_column('students', 'email')