```python
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'XXXX_add_email_to_student'
down_revision = None  # Update this to the last migration revision if necessary
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Add email column to the Student table."""
    # Adding the email column with NOT NULL constraint
    op.add_column('student', sa.Column('email', sa.String(), nullable=False))
    
    # Note: Perform data migration here if you have existing records and want to set a default value for email


def downgrade() -> None:
    """Remove email column from the Student table."""
    # Remove the email column if rolling back
    op.drop_column('student', 'email')
```