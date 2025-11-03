```python
"""CreateCourseTable Migration

This migration script adds the 'courses' table to the existing database schema.
The new table includes fields for course id, name, and level.

Revision ID: <timestamp>
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = None  # Change this based on your existing migrations
branch_labels = None
depends_on = None

def upgrade():
    """Apply the migration to create the 'courses' table."""
    op.create_table('courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )

def downgrade():
    """Revert the migration by dropping the 'courses' table."""
    op.drop_table('courses')
```