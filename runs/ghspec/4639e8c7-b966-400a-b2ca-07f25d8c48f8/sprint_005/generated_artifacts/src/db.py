```python
from alembic import op
import sqlalchemy as sa

# Migration script for creating the Teacher table.
def upgrade():
    # Create the 'teachers' table with 'id', 'name', and 'email' columns
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )

def downgrade():
    # Drop the 'teachers' table during a downgrade
    op.drop_table('teachers')
```