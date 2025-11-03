```python
"""Database Migration Script: Create Courses Table

This script creates a new 'courses' table in the database to manage course information.
The table includes fields for the course 'id', 'name', and 'level'.

The migration preserves existing data in the 'students' table.
"""

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '202310_create_courses_table'
down_revision = None  # Replace with the last revision identifier if applicable
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Apply the migration: create the courses table."""
    # Create the 'courses' table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('level', sa.String(length=100), nullable=False)
    )


def downgrade() -> None:
    """Revert the migration: drop the courses table."""
    # Drop the 'courses' table if it exists
    op.drop_table('courses')
```