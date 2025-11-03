```python
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# Revision identifiers, used by Alembic.
revision = '2023_10_01_add_email_to_student'
down_revision = None  # Update this according to your migration history
branch_labels = None
depends_on = None

def upgrade():
    """Add email field to the Student table."""
    # Add the new 'email' column to the 'students' table
    op.add_column('students', sa.Column('email', sa.String(length=255), nullable=False))

    # Here we could add data migration logic if necessary
    # For example, initializing email fields for existing students if required.


def downgrade():
    """Remove email field from the Student table."""
    # Remove the 'email' column during downgrade
    op.drop_column('students', 'email')
```