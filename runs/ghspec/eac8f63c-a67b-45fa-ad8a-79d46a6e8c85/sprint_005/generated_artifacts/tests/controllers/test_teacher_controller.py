```python
# tests/controllers/test_teacher_controller.py

from alembic import op
import sqlalchemy as sa

def upgrade():
    """Create the teachers table to store teacher information."""
    op.create_table('teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )

def downgrade():
    """Drop the teachers table if it exists."""
    op.drop_table('teachers')
```