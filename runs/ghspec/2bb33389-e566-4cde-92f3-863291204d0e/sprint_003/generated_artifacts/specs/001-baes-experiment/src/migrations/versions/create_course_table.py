```python
"""CreateCourseTable

Revision ID: 1234567890ab
Revises: 
Create Date: 2023-10-01 12:34:56.789012

"""

from alembic import op
import sqlalchemy as sa


def upgrade():
    """Create the courses table."""
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )


def downgrade():
    """Drop the courses table."""
    op.drop_table('courses')
```