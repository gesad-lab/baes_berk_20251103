```python
"""Create Teachers table

Revision ID: xxxxxxxx
Revises: 
Create Date: 2023-10-01 12:00:00.000000

"""
from alembic import op
from sqlalchemy import Column, Integer, String

# revision identifiers, used by Alembic.
revision = 'xxxxxxxx'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """Create the teachers table."""
    op.create_table(
        'teachers',  # The table name
        Column('id', Integer, primary_key=True, autoincrement=True),  # Primary key
        Column('name', String, nullable=False),  # Teacher's name
        Column('email', String, nullable=False, unique=True)  # Teacher's email, must be unique
    )


def downgrade():
    """Drop the teachers table."""
    op.drop_table('teachers')  # Remove the teachers table if downgrading
```