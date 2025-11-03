```python
"""Add email field to students table

Revision ID: <timestamp>
Revises: <previous_revision_id>
Create Date: <current_date>
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = '<previous_revision_id>'
branch_labels = None
depends_on = None

def upgrade():
    """Apply the upgrade to add the email column to the students table."""
    with op.batch_alter_table('students') as batch_op:
        # Adding the email column as a non-nullable field
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False))
        # Note: Ensure existing records will not violate this constraint.

def downgrade():
    """Revert the change by dropping the email column from the students table."""
    with op.batch_alter_table('students') as batch_op:
        batch_op.drop_column('email')
```