```python
"""Add email column to Student model

Revision ID: [timestamp]
Revises: 
Create Date: [timestamp]

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '[timestamp]'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """Apply the migration."""
    # Add the email column to the students table
    op.add_column('students', sa.Column('email', sa.String(length=255), nullable=False))


def downgrade():
    """Revert the migration."""
    # Remove the email column from the students table
    op.drop_column('students', 'email')
```