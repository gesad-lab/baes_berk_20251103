```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create the teachers table with required fields: id, name, email
    op.create_table('teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),  # Name is required
        sa.Column('email', sa.String(), nullable=False, unique=True)  # Email is required and must be unique
    )

def downgrade():
    # Drop the teachers table when rolling back the migration
    op.drop_table('teachers')
```