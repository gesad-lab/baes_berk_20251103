```python
"""Create Teachers Table

Revision ID: <timestamp>
Revises: 
Create Date: <timestamp>

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = None  # Update this if there is a previous revision
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create the Teachers table."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True)
    )


def downgrade() -> None:
    """Drop the Teachers table."""
    op.drop_table('teachers')
```