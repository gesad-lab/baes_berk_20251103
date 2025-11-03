```python
"""Migration script to add email column to the students table."""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'xxxx_add_email_to_students'  # Replace with your revision ID
down_revision = None  # Replace with your last migration ID
branch_labels = None
depends_on = None


def upgrade():
    """Apply the migration to add the email column."""
    # Add a new email column to the students table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
    # Create an index on the email column ensuring it is unique
    op.create_index('ix_email', 'students', ['email'], unique=True)


def downgrade():
    """Revert the migration by removing the email column."""
    # Drop the index on the email column
    op.drop_index('ix_email', table_name='students')
    # Drop the email column from the students table
    op.drop_column('students', 'email')
```