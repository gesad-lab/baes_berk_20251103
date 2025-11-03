```python
"""Add email field to students table.

Revision ID: 20230925_add_email_field
Revises: previous_revision_id
Create Date: 2023-09-25 12:00:00

"""

# revision identifiers, used by Alembic.
revision = '20230925_add_email_field'
down_revision = 'previous_revision_id'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    """Upgrade the database schema by adding the email field to the students table."""
    # Add the email column to the students table, allowing NULL values for existing records
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))


def downgrade():
    """Downgrade the database schema by removing the email field from the students table."""
    # Remove the email column from the students table
    op.drop_column('students', 'email')
```