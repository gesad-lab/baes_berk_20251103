```python
"""Create teachers table

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
    """Add the teachers table to the database."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True),
    )

def downgrade():
    """Drop the teachers table from the database."""
    op.drop_table('teachers')
```