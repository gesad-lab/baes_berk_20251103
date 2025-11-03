```python
from sqlalchemy import Column, String
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1_add_email'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Add email column to the students table."""
    op.add_column('students', sa.Column('email', sa.String(length=255), nullable=False))


def downgrade() -> None:
    """Remove email column from the students table."""
    op.drop_column('students', 'email')
```