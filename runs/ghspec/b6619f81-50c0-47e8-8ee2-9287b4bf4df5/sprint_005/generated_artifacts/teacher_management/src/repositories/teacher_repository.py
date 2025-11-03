```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create the teachers table with required fields
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),  # Primary key with auto-increment
        sa.Column('name', sa.String, nullable=False),                         # Teacher's name, required
        sa.Column('email', sa.String, nullable=False, unique=True)           # Teacher's email, required and must be unique
    )

def downgrade():
    # Drop the teachers table if it exists
    op.drop_table('teachers')
```