```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create the 'teachers' table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),  # Unique identifier for the teacher
        sa.Column('name', sa.String(length=100), nullable=False),  # Name of the teacher
        sa.Column('email', sa.String(length=100), nullable=False, unique=True)  # Unique email for the teacher
    )

def downgrade():
    # Drop the 'teachers' table if it exists
    op.drop_table('teachers')
```