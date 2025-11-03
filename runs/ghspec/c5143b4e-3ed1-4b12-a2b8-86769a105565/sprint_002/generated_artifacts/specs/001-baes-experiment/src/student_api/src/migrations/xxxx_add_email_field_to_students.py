from alembic import op
import sqlalchemy as sa
from src.models import Student  # Import the Student model for the context

# Revision identifiers, used by Alembic.
revision = 'xxxx_add_email_field_to_students'
down_revision = None  # Adjust this based on the last migration if applicable
branch_labels = None
depends_on = None

def upgrade():
    """Add email field to the students table."""
    # Adding the email column to the students table
    op.add_column('students', sa.Column('email', sa.String(length=256), nullable=False))

def downgrade():
    """Remove email field from the students table."""
    # Dropping the email column from the students table
    op.drop_column('students', 'email')