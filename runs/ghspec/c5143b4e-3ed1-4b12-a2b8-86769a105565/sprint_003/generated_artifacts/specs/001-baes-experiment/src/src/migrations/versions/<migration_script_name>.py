```python
"""Create Course table

Revision ID: <migration_script_name>
Revises: 
Create Date: YYYY-MM-DD HH:MM:SS.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<migration_script_name>'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    """Create the Course table in the database."""
    op.create_table(
        'courses',  # Name of the table
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),  # Auto-incrementing ID
        sa.Column('name', sa.String(length=100), nullable=False),  # Course name, must not be null
        sa.Column('level', sa.String(length=50), nullable=False)  # Course level, must not be null
    )

def downgrade():
    """Drop the Course table from the database."""
    op.drop_table('courses')
```