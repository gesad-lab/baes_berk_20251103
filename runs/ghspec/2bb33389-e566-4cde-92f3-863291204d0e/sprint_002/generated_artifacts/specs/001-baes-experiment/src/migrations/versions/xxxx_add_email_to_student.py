```python
"""Add email field to Student table.

Revision ID: xxxx_add_email_to_student
Revises: <previous_revision_id>
Create Date: <current_date>
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'xxxx_add_email_to_student'
down_revision = '<previous_revision_id>'  # Replace with the actual previous revision ID
branch_labels = None
depends_on = None


def upgrade():
    """Add the email column to the students table."""
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))


def downgrade():
    """Remove the email column from the students table."""
    op.drop_column('students', 'email')
```