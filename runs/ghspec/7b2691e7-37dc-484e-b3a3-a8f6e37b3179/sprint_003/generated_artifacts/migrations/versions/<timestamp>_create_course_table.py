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
down_revision = None  # Update if applicable to depend on previous migrations
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create the Course table."""
    op.create_table(
        'course',
        sa.Column('id', sa.Integer(), primary_key=True),  # Primary key for the Course table
        sa.Column('name', sa.String(length=100), nullable=False),  # Course name, required
        sa.Column('level', sa.String(length=50), nullable=False),  # Course level, required
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),  # Timestamp for creation
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now())  # Timestamp for last update
    )


def downgrade() -> None:
    """Drop the Course table."""
    op.drop_table('course')
```