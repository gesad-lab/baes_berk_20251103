```python
"""Add Courses Table Migration

This script adds a new 'courses' table to the database with columns for
'nam' and 'level'. The table will allow the application to manage
courses seamlessly without affecting existing student data.
"""

from alembic import op
from sqlalchemy import Column, String, Integer

# Revision identifiers, used by Alembic.
revision = '2023XXXXXX_add_courses_table'
down_revision = 'previous_revision_here'  # Update with the previous revision ID
branch_labels = None
depends_on = None

def upgrade():
    """Upgrade the database to include the courses table."""
    op.create_table(
        'courses',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String, nullable=False),
        Column('level', String, nullable=False)
    )

def downgrade():
    """Downgrade the database to remove the courses table."""
    op.drop_table('courses')
```