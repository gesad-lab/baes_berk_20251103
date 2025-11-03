```python
"""CreateTeachersTable

Revision ID: xxxxxx
Revises: 
Create Date: 2023-10-04 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'xxxxxx'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create the teachers table."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True)
    )


def downgrade() -> None:
    """Drop the teachers table."""
    op.drop_table('teachers')
```