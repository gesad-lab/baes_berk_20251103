```python
"""Add email field to student entity

Revision ID: xxxxxx
Revises: previous_revision_id
Create Date: 2023-10-08 12:00:00.000000
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxx'
down_revision = 'previous_revision_id'  # Replace with the actual previous revision ID
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Add the email column to the students table."""
    # Add the email column to the existing students table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade() -> None:
    """Remove the email column from the students table."""
    # Remove the email column during a downgrade
    op.drop_column('students', 'email')
```