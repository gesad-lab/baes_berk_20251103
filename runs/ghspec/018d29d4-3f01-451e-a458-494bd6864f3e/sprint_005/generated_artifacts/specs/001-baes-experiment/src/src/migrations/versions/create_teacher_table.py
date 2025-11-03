```python
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'create_teacher_table'
down_revision = None  # or the last migration revision
branch_labels = None
depends_on = None

def upgrade():
    """Create the teachers table with name and email columns."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),  # Unique ID for each teacher
        sa.Column('name', sa.String(), nullable=False),    # Teacher's name, required
        sa.Column('email', sa.String(), nullable=False, unique=True)  # Teacher's email, required and unique
    )

def downgrade():
    """Drop the teachers table."""
    op.drop_table('teachers')
```