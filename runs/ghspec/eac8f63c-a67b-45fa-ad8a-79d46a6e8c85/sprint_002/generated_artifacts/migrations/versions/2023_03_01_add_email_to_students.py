from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2023_03_01_add_email_to_students'
down_revision = None  # Update as necessary depending on your migration history
branch_labels = None
depends_on = None

def upgrade():
    """Apply the migration to add email field to students table."""
    # Add new column 'email' to 'students' table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
    # Ensure that email uniqueness is enforced
    op.create_unique_constraint('uq_email', 'students', ['email'])

def downgrade():
    """Revert the migration by removing email field from students table."""
    # Drop the email column from the 'students' table
    op.drop_column('students', 'email')