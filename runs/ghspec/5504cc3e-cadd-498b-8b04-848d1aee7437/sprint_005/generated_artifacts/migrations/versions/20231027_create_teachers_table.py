```python
"""Create teachers table

Revision ID: 20231027_create_teachers_table
Revises: 
Create Date: 2023-10-27 12:00:00
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20231027_create_teachers_table'
down_revision = None  # Adjust this if there's a previous migration
branch_labels = None
depends_on = None


def upgrade():
    """Create the teachers table."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),  # Unique identifier
        sa.Column('name', sa.String(length=255), nullable=False),  # Required name field
        sa.Column('email', sa.String(length=255), nullable=False, unique=True)  # Required unique email field
    )


def downgrade():
    """Drop the teachers table."""
    op.drop_table('teachers')
```