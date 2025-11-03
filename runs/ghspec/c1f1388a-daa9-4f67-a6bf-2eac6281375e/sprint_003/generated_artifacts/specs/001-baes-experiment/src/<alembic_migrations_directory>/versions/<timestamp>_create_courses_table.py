```python
"""create_courses_table

Revision ID: <timestamp>
Revises: 
Create Date: 2023-10-03 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = None  # Adjust according to your migration history
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Create the courses table."""
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )

def downgrade() -> None:
    """Drop the courses table."""
    op.drop_table('courses')
```