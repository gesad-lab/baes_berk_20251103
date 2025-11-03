```python
"""Create Teacher Table Migration

Revision ID: <revision_id>
Revises: <previous_revision_id>
Create Date: 2023-10-05 10:00:00
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<revision_id>'
down_revision = '<previous_revision_id>'
branch_labels = None
depends_on = None

def upgrade():
    """Apply the migration to create the teacher table."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )
    # Ensure the addition of new table does not affect existing student and course records

def downgrade():
    """Rollback the migration by dropping the teacher table."""
    op.drop_table('teachers')
```