from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_email_to_student'
down_revision = None  # Set this to the previous migration identifier
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Add email column to the Student table."""
    # Adding the 'email' column to the 'students' table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade() -> None:
    """Remove email column from the Student table."""
    # Dropping the 'email' column if we need to rollback
    op.drop_column('students', 'email')