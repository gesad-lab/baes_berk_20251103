```python
"""CreateCoursesTable

Revision ID: 2023_10_10
Revises: 
Create Date: 2023-10-10 12:00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2023_10_10'
down_revision = None  # Specify the previous revision ID or None for the first migration
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Upgrade the database to create the 'courses' table.

    This function creates the 'courses' table with `id`, `name`, and `level` columns.
    The `id` column is the primary key and auto-incremented.
    The `name` and `level` columns are required strings.
    """
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),  # The course name (required)
        sa.Column('level', sa.String, nullable=False)  # The course level (required)
    )


def downgrade() -> None:
    """Downgrade the database to remove the 'courses' table.

    This function drops the 'courses' table if it exists.
    """
    op.drop_table('courses')
```