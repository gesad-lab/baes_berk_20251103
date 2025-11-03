```python
"""Add email field to students table.

Revision ID: 004
Revises: 003
Create Date: 2023-10-03 12:00:00
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import SQLAlchemyError

# revision identifiers, used by Alembic.
revision = '004'
down_revision = '003'
branch_labels = None
depends_on = None

def upgrade():
    """Add the email column to the students table."""
    try:
        op.add_column('students', sa.Column('email', sa.String(), nullable=False))
    except SQLAlchemyError as e:
        # Log the error and raise an exception to prevent migration failure
        print(f"Error while adding email column: {str(e)}")
        raise

def downgrade():
    """Remove the email column from the students table."""
    try:
        op.drop_column('students', 'email')
    except SQLAlchemyError as e:
        # Log the error and raise an exception to prevent migration failure
        print(f"Error while dropping email column: {str(e)}")
        raise
```