```python
# migrations/002_create_teachers_table.py

from sqlalchemy import create_engine, Column, Integer, String
from alembic import op

def upgrade():
    """Create the teachers table in the database."""
    op.create_table(
        'teachers',
        Column('id', Integer, primary_key=True),  # Primary key
        Column('name', String, nullable=False),    # Teacher's name, cannot be null
        Column('email', String, nullable=False, unique=True)  # Teacher's email, must be unique and cannot be null
    )

def downgrade():
    """Drop the teachers table if it exists. This is used to reverse the upgrade."""
    op.drop_table('teachers')
```