```python
"""Create courses table

Revision ID: xxxx_create_courses_table
Revises: <previous_revision_id>
Create Date: <current_date>
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxx_create_courses_table'
down_revision = '<previous_revision_id>'
branch_labels = None
depends_on = None

def upgrade():
    """Create the courses table."""
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),  # Required field
        sa.Column('level', sa.String(), nullable=False),  # Required field
    )

def downgrade():
    """Drop the courses table."""
    op.drop_table('courses')
```