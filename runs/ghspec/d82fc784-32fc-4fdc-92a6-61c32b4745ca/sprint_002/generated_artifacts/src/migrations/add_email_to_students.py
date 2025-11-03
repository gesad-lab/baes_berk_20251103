from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20231002_add_email_to_students'
down_revision = '20231001_previous_migration'  # Replace with the actual previous migration ID
branch_labels = None
depends_on = None

def upgrade():
    """Add email column to the students table."""
    op.add_column('students', sa.Column('email', sa.String(length=254), nullable=True))  # Adds email column with a length constraint

def downgrade():
    """Remove email column from the students table."""
    op.drop_column('students', 'email')  # Reverts the addition of the email column
