from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_email_to_students'
down_revision = None  # Set accordingly if there's a previous migration
branch_labels = None
depends_on = None

def upgrade():
    """Add the 'email' column to the 'students' table."""
    # Add the new column 'email' with a NOT NULL constraint
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    """Remove the 'email' column from the 'students' table."""
    # Drop the 'email' column if we need to revert the migration
    op.drop_column('students', 'email')