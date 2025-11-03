```python
from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = 'add_email_field_to_students'
down_revision = None  # Set this to the last revision ID in your migration history
branch_labels = None
depends_on = None


def upgrade():
    """Upgrade the database schema by adding the email column to the students table."""
    # Adding the email column to the students table, it cannot be null.
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
    # Adding a unique constraint on the email field to ensure uniqueness.
    op.create_unique_constraint('uq_email', 'students', ['email'])


def downgrade():
    """Downgrade the database schema by removing the email column from the students table."""
    # Drop the email column if we need to downgrade the migration.
    op.drop_column('students', 'email')
```