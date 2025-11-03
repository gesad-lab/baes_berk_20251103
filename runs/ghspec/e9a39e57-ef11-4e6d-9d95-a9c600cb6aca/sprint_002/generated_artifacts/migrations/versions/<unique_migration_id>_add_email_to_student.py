```python
"""Add email field to Student table

Revision ID: <unique_migration_id>
Revises: 
Create Date: 2023-10-05 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '<unique_migration_id>'
down_revision = None  # Set this to the previous revision ID
branch_labels = None
depends_on = None


def upgrade():
    """Add email column to the students table and create a unique constraint."""
    # Add email column
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
    # Create unique constraint for the email field
    op.create_unique_constraint('uq_student_email', 'students', ['email'])


def downgrade():
    """Remove email column from the students table and drop the unique constraint."""
    # Drop unique constraint for the email field
    op.drop_constraint('uq_student_email', 'students', type_='unique')
    # Drop email column
    op.drop_column('students', 'email')
```