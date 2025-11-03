```python
"""Create courses table

Revision ID: <timestamp>
Revises: 
Create Date: <timestamp>

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = None  # Update to the previous migration if it exists
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Create the courses table"""
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )

def downgrade() -> None:
    """Drop the courses table"""
    op.drop_table('courses')
```