```python
"""CreateCourseTable

Revision ID: <timestamp>
Revises: 
Create Date: <timestamp>

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = None  # Change this to the latest migration revision if one exists
branch_labels = None
depends_on = None


def upgrade():
    """Create the Course table."""
    op.create_table(
        'course',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )


def downgrade():
    """Drop the Course table."""
    op.drop_table('course')
```