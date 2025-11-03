```python
"""Add email column to student table

Revision ID: xxxx_add_email_to_student
Revises: previous_revision_id
Create Date: 2023-10-01 00:00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'xxxx_add_email_to_student'
down_revision = 'previous_revision_id'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Add email column to the student table."""
    op.add_column('student', sa.Column('email', sa.String(length=255), nullable=True))
    # Implement email uniqueness constraint in future migrations if required
    # op.create_unique_constraint('uq_student_email', 'student', ['email'])


def downgrade() -> None:
    """Remove email column from the student table."""
    op.drop_column('student', 'email')
```