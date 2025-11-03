from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '2023XXXXXX'
down_revision = 'previous_revision_id'  # Replace with the actual previous revision ID
branch_labels = None
depends_on = None

def upgrade():
    """Apply the upgrade to add email field to the Student model."""
    # Adding the 'email' column to the 'students' table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False, unique=True))

def downgrade():
    """Revert the upgrade by removing the email field."""
    # Dropping the 'email' column from the 'students' table
    op.drop_column('students', 'email')