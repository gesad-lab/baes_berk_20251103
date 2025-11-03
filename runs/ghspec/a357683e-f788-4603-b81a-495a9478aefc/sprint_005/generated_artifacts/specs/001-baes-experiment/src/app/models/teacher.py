```python
"""Create teachers table

Revision ID: 123456789abc
Revises: None
Create Date: 2023-10-04 12:00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '123456789abc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Apply the migration to add the teachers table."""
    
    # Create the teachers table with specified columns
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),  # Auto-incrementing ID
        sa.Column('name', sa.String(length=100), nullable=False),  # Name cannot be null
        sa.Column('email', sa.String(length=100), nullable=False, unique=True)  # Email must be unique
    )


def downgrade() -> None:
    """Revert the migration by dropping the teachers table."""
    
    op.drop_table('teachers')
```