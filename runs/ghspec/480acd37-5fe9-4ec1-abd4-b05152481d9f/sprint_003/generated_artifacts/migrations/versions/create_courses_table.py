```python
"""create_courses_table.py

This migration script creates the 'courses' table, which includes fields for id, 
name, and level. This table is used to store course records in the database.

Revision ID: 123456789abc
Revises: 
Create Date: 2023-10-03 12:00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '123456789abc'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Apply the migration to create the 'courses' table."""
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),  # Required field
        sa.Column('level', sa.String, nullable=False)  # Required field
    )

def downgrade() -> None:
    """Revert the migration by dropping the 'courses' table."""
    op.drop_table('courses')
```