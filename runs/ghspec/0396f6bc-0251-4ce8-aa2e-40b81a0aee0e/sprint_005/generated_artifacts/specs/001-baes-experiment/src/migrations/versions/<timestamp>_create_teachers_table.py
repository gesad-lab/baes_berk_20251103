```python
"""create_teachers_table

Revision ID: <timestamp>
Revises: 
Create Date: 2023-10-06 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = None  # Update this based on your last revision
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create the teachers table with the specified fields."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True)
    )
    # Note: Existing data from other tables (e.g., Students, Courses) is preserved.


def downgrade() -> None:
    """Drop the teachers table during a rollback."""
    op.drop_table('teachers')
```