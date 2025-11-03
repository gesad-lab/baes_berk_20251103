```python
"""Add email field to the Student model.

Revision ID: 20231010_add_email_field
Revises: previous_revision_id  # Replace with actual revision ID if available.
Create Date: 2023-10-10 12:00:00.000000
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20231010_add_email_field'
down_revision = 'previous_revision_id'  # Replace with actual revision ID if available.
branch_labels = None
depends_on = None


def upgrade():
    """Add the email column to the students table."""
    # Adding a new email column that cannot be null.
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))


def downgrade():
    """Remove the email column from the students table."""
    # Dropping the email column in case of a downgrade.
    op.drop_column('students', 'email')
```