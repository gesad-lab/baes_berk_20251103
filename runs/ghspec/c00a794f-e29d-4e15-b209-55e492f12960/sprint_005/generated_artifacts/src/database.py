```python
# src/database.py

from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create the 'teachers' table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),  # Required field for teacher's name
        sa.Column('email', sa.String(), nullable=False)  # Required field for teacher's email
    )

def downgrade():
    # Drop the 'teachers' table if it exists
    op.drop_table('teachers')
```