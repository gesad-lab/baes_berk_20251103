```python
# migrations/add_teachers_table.py

from alembic import op
import sqlalchemy as sa

# Migration to create the teachers table in the database schema
def upgrade():
    # Create the teachers table with the specified fields and constraints
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),  # ID as primary key
        sa.Column('name', sa.String, nullable=False),  # Name must be provided
        sa.Column('email', sa.String, nullable=False, unique=True),  # Email must be unique and provided
    )

def downgrade():
    # Drop the teachers table if the migration is reversed
    op.drop_table('teachers')
```