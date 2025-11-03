```python
"""Add email field to students table.

This migration will add a new column 'email' to the students
table to store the email addresses of students. It will preserve
existing data and ensure the new column can hold valid email
addresses.
"""

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'xxxx_add_email_to_students'
down_revision = 'previous_revision_id'  # Replace with the actual previous revision ID
branch_labels = None
depends_on = None

def upgrade():
    """Apply the migration by adding an 'email' column to the students table."""
    # Add a new column 'email' that allows nullable values
    op.add_column('students', sa.Column('email', sa.String(length=255), nullable=True))

def downgrade():
    """Reverse the migration by dropping the 'email' column from the students table."""
    op.drop_column('students', 'email')
```