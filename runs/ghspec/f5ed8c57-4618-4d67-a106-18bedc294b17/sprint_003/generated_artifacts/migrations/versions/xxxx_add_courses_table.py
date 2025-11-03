```python
"""add_courses_table

Revision ID: xxxx
Revises: None
Create Date: 2023-10-01 12:00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxx'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Add the courses table to the database."""
    # Create the 'courses' table with the required fields
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )


def downgrade() -> None:
    """Remove the courses table from the database."""
    # Drop the 'courses' table if it exists
    op.drop_table('courses')
```