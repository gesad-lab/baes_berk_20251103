```python
"""create_teachers_table.py

This migration script creates the teachers table in the database
with appropriate fields and constraints to store teacher information.
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxxxxxxxx'
down_revision = 'yyyyyyyyyyyy'  # replace with the last migration ID
branch_labels = None
depends_on = None

def upgrade():
    """Create the teachers table."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )

def downgrade():
    """Drop the teachers table."""
    op.drop_table('teachers')
```