```python
"""Add email column to students table.

Revision ID: <revision_id>
Revises: <base_revision_id>
Create Date: <date_time>
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '<revision_id>'
down_revision = '<base_revision_id>'
branch_labels = None
depends_on = None


def upgrade():
    """Add email column to students table."""
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))


def downgrade():
    """Remove email column from students table."""
    op.drop_column('students', 'email')
```