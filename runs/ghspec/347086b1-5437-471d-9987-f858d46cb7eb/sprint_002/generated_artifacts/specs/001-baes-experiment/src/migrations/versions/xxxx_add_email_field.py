# migrations/versions/xxxx_add_email_field.py

"""Add email field to students table

Revision ID: xxxx
Revises: (previous revision)
Create Date: (create date)
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxx'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Apply the migration to add the email column to the students table."""
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))

def downgrade() -> None:
    """Revert the migration by dropping the email column from the students table."""
    op.drop_column('students', 'email')