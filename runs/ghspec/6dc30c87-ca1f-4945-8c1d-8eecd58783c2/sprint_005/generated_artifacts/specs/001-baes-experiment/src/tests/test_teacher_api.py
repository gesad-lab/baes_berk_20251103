```python
"""Create teachers table

Revision ID: 123456789abc
Revises: <previous_revision_id>
Create Date: 2023-10-02 12:00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '123456789abc'
down_revision = '<previous_revision_id>'
branch_labels = None
depends_on = None


def upgrade():
    """Add the teachers table to the database schema."""
    # Creating the 'teachers' table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),  # Auto-incrementing primary key
        sa.Column('name', sa.String, nullable=False),   # Required field
        sa.Column('email', sa.String, nullable=False, unique=True),  # Required and unique
    )


def downgrade():
    """Drop the teachers table if it exists."""
    # Dropping the 'teachers' table in case of downgrade
    op.drop_table('teachers')
```