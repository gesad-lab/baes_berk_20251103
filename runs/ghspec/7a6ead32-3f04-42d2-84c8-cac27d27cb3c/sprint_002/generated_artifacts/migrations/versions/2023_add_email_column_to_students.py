```python
"""Add email column to students table

Revision ID: xyz
Revises: previous_revision_id
Create Date: 2023-10-10 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xyz'
down_revision = 'previous_revision_id'
branch_labels = None
depends_on = None

def upgrade():
    # Add the email column to the students table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    # Remove the email column during a rollback
    op.drop_column('students', 'email')
```