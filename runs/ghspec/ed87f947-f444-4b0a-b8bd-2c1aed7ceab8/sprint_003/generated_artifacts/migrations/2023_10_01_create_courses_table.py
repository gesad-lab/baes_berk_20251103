```python
"""CreateCoursesTable Migration Script

This script creates the 'courses' table in the database with the following fields:
- id: Primary key that auto-increments
- name: Required string indicating the name of the course
- level: Required string indicating the course level
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2023_10_01_create_courses_table'
down_revision = None  # or the previous migration ID if applicable
branch_labels = None
depends_on = None

def upgrade():
    """Apply the migration to create the courses table."""
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('level', sa.String, nullable=False),
    )

def downgrade():
    """Revert the migration by dropping the courses table."""
    op.drop_table('courses')
```