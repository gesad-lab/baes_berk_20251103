```python
"""Add teachers table

Revision ID: xxxx
Revises: 
Create Date: 2023-10-04 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxx'
down_revision = None  # Update with the correct previous revision ID
branch_labels = None
depends_on = None


def upgrade():
    """Create the teachers table."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False)
    )


def downgrade():
    """Drop the teachers table."""
    op.drop_table('teachers')
```