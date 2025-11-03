```python
"""CreateCoursesTable Migration

This migration script creates the 'courses' table in the database with the specified 
columns: id, name, and level. The id is an auto-generated primary key, while name and 
level are required string fields.
"""

from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = '20230320_create_courses_table'
down_revision = None  # Adjust this if you have other migrations
branch_labels = None
depends_on = None


def upgrade():
    """Upgrade the database: create the 'courses' table."""
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )


def downgrade():
    """Downgrade the database: drop the 'courses' table."""
    op.drop_table('courses')
```