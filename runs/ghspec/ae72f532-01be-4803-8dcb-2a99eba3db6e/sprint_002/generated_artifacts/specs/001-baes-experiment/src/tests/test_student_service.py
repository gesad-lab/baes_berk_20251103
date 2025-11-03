```python
from alembic import op
import sqlalchemy as sa


def upgrade():
    """Add email column to the students table."""
    # Add the email column, setting it as a non-nullable field
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))


def downgrade():
    """Drop email column from the students table."""
    # Reverse the upgrade by dropping the email column
    op.drop_column('students', 'email')
```