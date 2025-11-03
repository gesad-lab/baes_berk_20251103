# migrations/versions/xxxx_add_email_to_students.py
from alembic import op
import sqlalchemy as sa

def upgrade():
    """Add email column to the students table."""
    # Ensure that we add an email column which is required (not null).
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    """Remove email column from the students table."""
    # Revert the migration by dropping the email column safely.
    op.drop_column('students', 'email')