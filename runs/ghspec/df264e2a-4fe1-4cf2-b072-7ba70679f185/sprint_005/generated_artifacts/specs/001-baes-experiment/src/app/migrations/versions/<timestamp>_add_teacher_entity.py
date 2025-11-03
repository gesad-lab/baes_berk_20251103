```python
"""Add Teacher entity."""

# Import required modules for Alembic migration
from alembic import op
import sqlalchemy as sa

# Revision identifiers
revision = '<timestamp>'  # Replace with actual timestamp
down_revision = None  # Set this if you have a prior revision
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Create the teachers table in the database."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )

def downgrade() -> None:
    """Drop the teachers table from the database."""
    op.drop_table('teachers')
```