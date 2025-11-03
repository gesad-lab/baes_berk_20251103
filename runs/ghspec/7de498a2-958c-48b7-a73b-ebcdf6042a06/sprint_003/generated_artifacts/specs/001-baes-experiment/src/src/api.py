```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create the 'courses' table with 'id', 'name', and 'level' columns
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),  # Course name is required
        sa.Column('level', sa.String(), nullable=False)  # Course level is required
    )

def downgrade():
    # Drop the 'courses' table if it exists
    op.drop_table('courses')
```